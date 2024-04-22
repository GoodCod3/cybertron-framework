from src.core.environment.environment import Environment
from src.core.input.input_manager_interface import IInputManager


class GlobalInputManager(IInputManager):
    def __init__(self):
        environment = Environment()  # noqa: F841

    def get_id(self):
        return "global"

    def get_data(self):
        return []
