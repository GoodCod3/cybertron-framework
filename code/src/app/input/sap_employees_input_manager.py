from datetime import date
from src.core.environment.environment import Environment
from src.core.input.input_manager_interface import IInputManager
from src.include.sap_client import SapClient

class SapEmployeesInputManager(IInputManager):

    def __init__(self):
        environment = Environment()
        host = environment.get_value("SAP_API_HOST")
        user = environment.get_value("SAP_API_USER")
        password = environment.get_value("SAP_API_PASS")
        endpoint = environment.get_value("SAP_API_GET_EMPLOYEES_ENDPOINT")
        self.filter_month = environment.get_value("FILTER_MONTH")
        self.filter_year = environment.get_value("FILTER_YEAR")
        self.sap_client = SapClient(host, user, password, endpoint)

    def get_id(self):
        return "sap_employees"

    def get_data(self):
        return self.sap_client.get_employees(date.today().strftime("%m"), date.today().strftime("%Y"))
