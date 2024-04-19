from src.core.environment.environment import Environment
from src.core.input.input_manager_interface import IInputManager
from src.include.successfactors_api import SuccessFactorsApi

class GlobalInputManager(IInputManager):

    def __init__(self):
        environment = Environment()
        host = environment.get_value("SF_API_HOST")
        user = environment.get_value("SF_API_USER")
        password = environment.get_value("SF_API_PASS")
        endpoint = environment.get_value("SF_API_ENDPOINT_GLOBAL")
        parameters = environment.get_value("SF_API_ENDPOINT_GLOBAL_PARAMS")
        self.successfactors_api = SuccessFactorsApi(host, user, password, endpoint, parameters)

    def get_id(self):
        return "global"

    def get_data(self):
        return self.successfactors_api.get_data()
