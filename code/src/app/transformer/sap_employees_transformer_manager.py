import re
from datetime import datetime
from src.app.transformer.abstract_transformer_manager import AbstractTransformerManager
from src.core.mapper.mapper_manager_interface import IMapperManager

class SapEmployeesTransformerManager(AbstractTransformerManager):

    def __init__(self):
        exclusions = {
            "user_id": {
                "value": "10000000",
                "operator": "EQUALS",
            }
        }
        super().__init__(exclusions)

    def get_id(self):
        return "sap_employees"
