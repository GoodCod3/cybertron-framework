from src.core.mapper.mapper_manager_interface import IMapperManager

class SapEmployeesMapperManager(IMapperManager):
    """
    SapEmployees mapper manager
    """

    DATA_MAPPER = [
       {
            "destination": {
                "field_name": "user_id",
                "type": "STRING",
            },
            "source": {
                "field_name": "PersonExternalID",
                "type": "text",
            },
        },
       {
            "destination": {
                "field_name": "sap_user_id",
                "type": "STRING",
            },
            "source": {
                "field_name": "Person",
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "full_name",
                "type": "STRING",
            },
            "source": {
                "field_name": "PersonFullName",
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "email",
                "type": "STRING",
            },
            "source": {
                "field_name": "DefaultEmailAddress",
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "company_code",
                "type": "STRING",
            },
            "source": {
                "field_name": "CompanyCode",
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "cost_center",
                "type": "STRING",
            },
            "source": {
                "field_name": "CostCenter",
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "person_work_agreement",
                "type": "STRING",
            },
            "source": {
                "field_name": "PersonWorkAgreement_1",
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "work_agreement_status",
                "type": "STRING",
            },
            "source": {
                "field_name": "WorkAgreementStatus",
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "start_date",
                "type": "STRING",
            },
            "source": {
                "field_name": "StartDate",
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "end_date",
                "type": "STRING",
            },
            "source": {
                "field_name": "EndDateDate",
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "orgl_details_start_date",
                "type": "STRING",
            },
            "source": {
                "field_name": "OrglDetailsStartDate",
                "type": "text",
            },
        },
        {
            "destination": {
                "field_name": "orgl_details_end_date",
                "type": "STRING",
            },
            "source": {
                "field_name": "OrglDetailsEndDate",
                "type": "text",
            },
        },
    ]

    def get_id(self):
        return "sap_employees"

    def get(self):
        return self.DATA_MAPPER

    def get_flattened(self):
        return self.DATA_MAPPER
