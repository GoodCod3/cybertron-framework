from src.core.input.input_manager_interface import IInputManager


class FirstInputManager(IInputManager):
    def get_id(self):
        return "global"

    def get_data(self):
        return []
