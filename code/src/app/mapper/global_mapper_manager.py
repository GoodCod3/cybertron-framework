from src.core.mapper.mapper_manager_interface import IMapperManager

class GlobalMapperManager(IMapperManager):
    """
    Global mapper manager
    """

    DATA_MAPPER = []

    def get_id(self):
        return "global"

    def get(self):
        return self.DATA_MAPPER

    def get_flattened(self):
        return self.get()
