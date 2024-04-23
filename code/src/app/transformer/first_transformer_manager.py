from src.core.mapper.mapper_manager_interface import IMapperManager
from src.core.transformer.transformer_manager_interface import (
    ITransformerManager,
)


class FirstTransformerManager(ITransformerManager):
    def __init__(self, exclusions={}):
        self.mapper_manager = None
        self.exclusions = exclusions

    def get_id(self):
        return "global"

    def set_mapper_manager(self, mapper_manager):
        if not isinstance(mapper_manager, IMapperManager):
            raise TypeError(
                "The provided MapperManager does not implement the IMapperManager interface."  # noqa: E501
            )

        self.mapper_manager = mapper_manager

    def transform(self, data):
        self.is_initialized()

        return self.transform_data(data)

    def is_initialized(self):
        if self.mapper_manager is None:
            raise RuntimeError("No MapperManager defined.")

    def transform_data(self, data):
        """
        Transforms the data
        """
        transformed_data = []

        return transformed_data
