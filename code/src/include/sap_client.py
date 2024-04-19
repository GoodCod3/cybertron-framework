import os
import json
import calendar
from .rest_client import RestClient
from src.core.environment.environment import Environment
from src.core.helper.logger import Logger
from src.core.exception.abort_process_exception import AbortProcessException


class SapClient:
    """
    Handles the communication with SAP
    """

    def __init__(self, host, user, password, endpoint):
        self.environment = Environment()
        self.sap_api_host = host
        self.sap_api_get_employees_endpoint = endpoint
        sap_api_user = user
        sap_api_pass = password
        self.rest_client = RestClient(sap_api_user, sap_api_pass)
        self.logger = Logger()

    def __get_data(self, endpoint, parameters):
        """
        Gets data from SAP
        """
        response = self.rest_client.get(self.sap_api_host + endpoint + parameters)

        return response if response.status_code == 200 else False

    def __group_employees(self, employees, grouping_attribute, fallback_grouping_attribute):
        """
        Groups employees
        """
        grouped_employees = {}
        for employee in employees:
            if employee['WorkAgreementStatus'] != '1':
                continue

            employee_id = employee[grouping_attribute]

            if not employee_id:
                employee_id = employee[fallback_grouping_attribute]

            if not employee_id in grouped_employees:
                grouped_employees[employee_id] = []

            grouped_employees[employee_id].append(employee)

        return grouped_employees

    def __get_employees_by_least_company_code(self, employee_group, filter_field):
        """
        Gets the employees with the least company code of a given group
        """
        value = employee_group[0][filter_field]
        for employee in employee_group:
            if employee[filter_field] < value:
                value = employee[filter_field]

        selected_employees = []
        for employee in employee_group:
            if employee[filter_field] == value:
                selected_employees.append(employee)

        return selected_employees

    def __get_last_employee(self, employee_group, filter_field):
        """
        Gets the last employee of a given group
        """
        if len(employee_group) == 1:
            return employee_group[0]

        selected_employee = employee_group[0]
        value = selected_employee[filter_field]
        for employee in employee_group:
            if employee[filter_field] > value:
                selected_employee = employee
                value = employee[filter_field]

        return selected_employee

    def __filter_employees(self, employees):
        """
        Filters the employees
        We take the latest PersonWorkAgreement_1
        """
        filtered_employees = []
        grouped_employees = self.__group_employees(employees, "DefaultEmailAddress", "PersonWorkAgreement_1")
        for employee_group in grouped_employees:
            employees_of_least_company = self.__get_employees_by_least_company_code(grouped_employees[employee_group], "CompanyCode")
            last_employee = self.__get_last_employee(employees_of_least_company, "PersonWorkAgreement_1")
            filtered_employees.append(last_employee)

        return filtered_employees

    def __build_date_params(self, month, year):
        """
        Builds the date parameters for the employees query
        """
        if not isinstance(month, int):
            month = int(month)
        if not isinstance(year, int):
            year = int(year)
        monthrange = calendar.monthrange(year, month)
        month = str(month)
        last_day = str(monthrange[1])
        start_date = f"{year}-{month.zfill(2)}-01"
        end_date = f"{year}-{month.zfill(2)}-{last_day.zfill(2)}"

        return f"?StartDate={end_date}&EndDate={start_date}"

    def __log_discarded_employees(self, employees, filtered_employees):
        """
        Logs the discarded employees
        """
        discarded_employees_count = len(employees) - len(filtered_employees)
        if discarded_employees_count == 0:
            return

        discarded_employees = []
        for employee in employees:
            email = employee["DefaultEmailAddress"]
            person_work_agreement = employee["PersonWorkAgreement_1"]
            for filtered_employee in filtered_employees:
                if filtered_employee["DefaultEmailAddress"] == email:
                    if employee != filtered_employee:
                        discarded_employees.append(employee)

        self.logger.info(f"De {len(employees)} empleados totales, hemos filtrado {discarded_employees_count}. Empleados descartados: {str(discarded_employees)}")

    def get_employees(self, month, year):
        """
        Retrieves the employees registered in SAP
        """
        response = self.__get_data(self.sap_api_get_employees_endpoint, self.__build_date_params(month, year))
        if not response:
            raise Exception(f"El servicio de consulta de empleados de SAP ha fallado: Es probable que las variables de entorno no estén correctamente configuradas.")
        else:
            response_object = json.loads(response.content)
            if not "YY1_Employee_WorkAgreement" in response_object:
                raise Exception("El servicio de consulta de empleados de SAP ha devuelto datos corruptos")
            if not "YY1_Employee_WorkAgreementType" in response_object["YY1_Employee_WorkAgreement"]:
                raise Exception("El servicio de consulta de empleados de SAP no ha devuelto resultados")

            employees = response_object["YY1_Employee_WorkAgreement"]["YY1_Employee_WorkAgreementType"]
            filtered_employees = self.__filter_employees(employees)
            self.__log_discarded_employees(employees, filtered_employees)

            return filtered_employees
