from src.app.transformer.abstract_transformer_manager import (
    AbstractTransformerManager,
)


class GlobalTransformerManager(AbstractTransformerManager):
    def __init__(self):
        exclusions = {}
        super().__init__(exclusions)

    def get_id(self):
        return "global"
