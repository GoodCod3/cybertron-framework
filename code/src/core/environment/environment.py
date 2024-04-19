import os
import yaml
from src.core.environment.environment_interface import IEnvironment

class Environment(IEnvironment):
    """
    Generic environment functions
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):
        if self._instance is not None:
            return

        self.environment_variables = None
        self.config_variables = None

    def set_environment_variables(self, environment_variables):
        self.environment_variables = environment_variables

    def set_configuration_file(self, configuration_file_path):
        with open(configuration_file_path, 'r') as config_file:
            self.config_variables = yaml.safe_load(config_file)

    def check(self):
        for environment_variable in self.environment_variables:
            value = os.getenv(environment_variable)
            if not value:
                raise RuntimeError(f"Environment variable not defined: {environment_variable}")

    def get_value(self, key):
        if key in self.config_variables:
            return self.config_variables[key]
        elif os.getenv(key):
            return os.getenv(key)

        return None
