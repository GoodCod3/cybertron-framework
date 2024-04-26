from src.app.resources.first_entry.constants import PROCESS_NAME
from src.core.transformer.transformer_manager_interface import (
    ITransformerManager,
)


class FirstTransformerManager(ITransformerManager):
    def __init__(self, exclusions={}):
        self.mapper_manager = None
        self.exclusions = exclusions

    def get_id(self):
        return PROCESS_NAME

    def transform(self, data):
        return self.transform_data(data)

    def transform_data(self, data):
        """
        Transforms the data
        """
        transformed_data = []

        return transformed_data
