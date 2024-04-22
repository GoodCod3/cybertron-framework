from src.core.environment.environment import Environment
from src.core.output.output_manager_interface import IOutputManager

class GlobalOutputManager(IOutputManager):

    def __init__(self):
        environment = Environment()
        self.project = environment.get_value("BIGQUERY_PROJECT")
        self.dataset = environment.get_value("BIGQUERY_DATASET")
        self.table_name = environment.get_value("BIGQUERY_TABLE_GLOBAL")
        super().__init__()

    def get_id(self):
        return "global"
