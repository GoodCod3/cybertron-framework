from src.core.input.input_manager_interface import IInputManager
from src.app.resources.first_entry.constants import PROCESS_NAME


class FirstInputManager(IInputManager):
    def get_id(self):
        return PROCESS_NAME

    def get_data(self):
        # Here the request will be made to the external source
        # (API, db, etc.) to obtain the data.
        return []
