from typing import List

from src.core.environment.environment import Environment
from src.core.output.output_manager_interface import IOutputManager
from src.core.mapper.mapper_manager_interface import IMapperManager


class GlobalOutputManager(IOutputManager):
    def __init__(self):
        environment = Environment()
        self.project = environment.get_value("BIGQUERY_PROJECT")
        self.dataset = environment.get_value("BIGQUERY_DATASET")
        self.table_name = environment.get_value("BIGQUERY_TABLE_GLOBAL")
        super().__init__()

    def get_id(self):
        return "global"

    def set_mapper_manager(self, mapper_manager: IMapperManager):
        pass

    def put(self, data: List[dict]):
        pass
