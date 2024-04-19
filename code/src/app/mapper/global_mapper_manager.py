from src.core.mapper.mapper_manager_interface import IMapperManager

class GlobalMapperManager(IMapperManager):
    """
    Global mapper manager
    """

    DATA_MAPPER = [
        {
            "destination": {
                "field_name": "person_id",
                "type": "STRING",
            },
            "source": {
                "field_name": ["employmentNav", "personNav", "personId"],
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "user_id",
                "type": "STRING",
            },
            "source": {
                "field_name": "userId",
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "assignment_id_external",
                "type": "STRING",
            },
            "source": {
                "field_name": ["employmentNav", "assignmentIdExternal"],
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "email_address",
                "type": "STRING",
            },
            "source": {
                "field_name": ["employmentNav", "personNav", "emailNav", "results"],
                "type": "filter",
                "filter_definition": {
                    "criteria": ["__metadata", "uri"],
                    "matching": "contains",
                    "value": "emailType='4049'",
                    "source_field": "emailAddress",
                },
            },
        },
        {
            "destination": {
                "field_name": "global_effective_start_date",
                "type": "STRING",
            },
            "source": {
                "field_name": "startDate",
                "type": "date",
            },
        },
        {
            "destination": {
                "field_name": "global_effective_end_date",
                "type": "STRING",
            },
            "source": {
                "field_name": "endDate",
                "type": "date",
            },
        },
        {
            "destination": {
                "field_name": "global_event_reason",
                "type": "STRING",
            },
            "source": {
                "field_name": ["eventReasonNav", "name"],
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "global_standard_weekly_hours",
                "type": "STRING",
            },
            "source": {
                "field_name": "standardHours",
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "global_fte",
                "type": "STRING",
            },
            "source": {
                "field_name": "fte",
                "type": "special_fte",
            },
        },
        {
            "destination": {
                "field_name": "global_company_external_code",
                "type": "STRING",
            },
            "source": {
                "field_name": "customString21",
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "global_company_code",
                "type": "STRING",
            },
            "source": {
                "field_name": "company",
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "global_company_name",
                "type": "STRING",
            },
            "source": {
                "field_name": ["companyNav", "name"],
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "global_service_type",
                "type": "STRING",
            },
            "source": {
                "field_name": "businessUnit",
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "global_service_type_name",
                "type": "STRING",
            },
            "source": {
                "field_name": ["businessUnitNav", "name"],
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "global_business_unit",
                "type": "STRING",
            },
            "source": {
                "field_name": "division",
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "global_business_unit_name",
                "type": "STRING",
            },
            "source": {
                "field_name": ["divisionNav", "name"],
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "global_department",
                "type": "STRING",
            },
            "source": {
                "field_name": "department",
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "global_department_name",
                "type": "STRING",
            },
            "source": {
                "field_name": ["departmentNav", "name"],
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "global_new_cost_center",
                "type": "STRING",
            },
            "source": {
                "field_name": "customString12",
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "global_cost_center",
                "type": "STRING",
            },
            "source": {
                "field_name": ["positionNav", "cust_Cost_Center"],
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "global_cost_center_name",
                "type": "STRING",
            },
            "source": {
                "field_name": ["costCenterNav", "name"],
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "global_team",
                "type": "STRING",
            },
            "source": {
                "field_name": "customString1",
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "global_supervisor",
                "type": "STRING",
            },
            "source": {
                "field_name": "managerId",
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "global_paygrade",
                "type": "STRING",
            },
            "source": {
                "field_name": "payGrade",
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "global_paygrade_name",
                "type": "STRING",
            },
            "source": {
                "field_name": ["payGradeNav", "name"],
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "global_location",
                "type": "STRING",
            },
            "source": {
                "field_name": "location",
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "global_location_name",
                "type": "STRING",
            },
            "source": {
                "field_name": ["locationNav", "name"],
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "global_holiday_calendar_code",
                "type": "STRING",
            },
            "source": {
                "field_name": ["holidayCalendarCodeNav", "name_defaultValue"],
                "type": "special_holiday_calendar",
            },
        },
        {
            "destination": {
                "field_name": "global_employee_class",
                "type": "STRING",
            },
            "source": {
                "field_name": "employeeClass",
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "global_employee_class_name",
                "type": "STRING",
            },
            "source": {
                "field_name": ["employeeClassNav", "picklistLabels", "results", 0, "label"],
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "global_employment_type",
                "type": "STRING",
            },
            "source": {
                "field_name": "employmentType",
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "global_employment_type_name",
                "type": "STRING",
            },
            "source": {
                "field_name": ["employmentTypeNav", "picklistLabels", "results", 0, "label"],
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "global_employee_status",
                "type": "STRING",
            },
            "source": {
                "field_name": "emplStatus",
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "global_employee_status_name",
                "type": "STRING",
            },
            "source": {
                "field_name": ["emplStatusNav", "picklistLabels", "results", 0, "label"],
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "employment_hire_date",
                "type": "STRING",
            },
            "source": {
                "field_name": "hireDate",
                "type": "date",
            },
        },
        {
            "destination": {
                "field_name": "employment_internship_start_date",
                "type": "STRING",
            },
            "source": {
                "field_name": ["employmentNav", "customDate1"],
                "type": "date",
            },
        },
        {
            "destination": {
                "field_name": "employment_internship_end_date",
                "type": "STRING",
            },
            "source": {
                "field_name": ["employmentNav", "customDate2"],
                "type": "date",
            },
        },
        {
            "destination": {
                "field_name": "employment_original_start_date",
                "type": "STRING",
            },
            "source": {
                "field_name": ["employmentNav", "originalStartDate"],
                "type": "date",
            },
        },
        {
            "destination": {
                "field_name": "employment_last_date_worked",
                "type": "STRING",
            },
            "source": {
                "field_name": ["employmentNav", "lastDateWorked"],
                "type": "date",
            },
        },
        {
            "destination": {
                "field_name": "employment_termination_date",
                "type": "STRING",
            },
            "source": {
                "field_name": "terminationDate",
                "type": "date",
            },
        },
        {
            "destination": {
                "field_name": "employment_contingent_worker",
                "type": "STRING",
                "default_value": "False"
            },
            "source": {
                "field_name": ["employmentNav", "isContingentWorker"],
                "type": "text",
            },
        },
    ]

    def get_id(self):
        return "global"

    def get(self):
        return self.DATA_MAPPER

    def get_flattened(self):
        return self.DATA_MAPPER
