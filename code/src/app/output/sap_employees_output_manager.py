from src.core.environment.environment import Environment
from src.app.output.abstract_output_manager import AbstractOutputManager

class SapEmployeesOutputManager(AbstractOutputManager):

    def __init__(self):
        environment = Environment()
        environment = Environment()
        self.project = environment.get_value("BIGQUERY_PROJECT")
        self.dataset = environment.get_value("BIGQUERY_DATASET")
        self.table_name = environment.get_value("BIGQUERY_TABLE_EMPLOYEES")
        super().__init__()

    def get_id(self):
        return "sap_employees"
