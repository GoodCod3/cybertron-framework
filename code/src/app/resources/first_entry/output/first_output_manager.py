from typing import List

from src.core.environment.environment import Environment
from src.core.output.output_manager_interface import IOutputManager
from src.app.resources.first_entry.constants import PROCESS_NAME


class FirstOutputManager(IOutputManager):
    def __init__(self):
        environment = Environment()
        self.project = environment.get_value("BIGQUERY_PROJECT")
        self.dataset = environment.get_value("BIGQUERY_DATASET")
        self.table_name = environment.get_value("BIGQUERY_TABLE_GLOBAL")
        super().__init__()

    def get_id(self):
        return PROCESS_NAME

    def put(self, data: List[dict]):
        # Here we will process all the transformed information
        # (Export to db, Bigquery, Pub/Sub, etc...)
        pass
