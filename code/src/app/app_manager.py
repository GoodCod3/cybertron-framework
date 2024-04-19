from src.core.app_manager_interface import IAppManager
from src.core.orchestrator.orchestrator_interface import IOrchestrator
from src.core.environment.environment_interface import IEnvironment
from src.core.environment.environment import Environment
from src.app.orchestrator.orchestrator import Orchestrator

from src.app.mapper.global_mapper_manager import GlobalMapperManager
from src.app.mapper.sap_employees_mapper_manager import SapEmployeesMapperManager

from src.app.input.global_input_manager import GlobalInputManager
from src.app.input.sap_employees_input_manager import SapEmployeesInputManager

from src.app.transformer.global_transformer_manager import GlobalTransformerManager
from src.app.transformer.sap_employees_transformer_manager import SapEmployeesTransformerManager

from src.app.output.global_output_manager import GlobalOutputManager
from src.app.output.sap_employees_output_manager import SapEmployeesOutputManager

class AppManager(IAppManager):
    """
    Application manager
    """

    def __init__(self):
        self.orchestrator = Orchestrator()
        self.environment = Environment()

    def __is_orchestrator(self):
        if not isinstance(self.orchestrator, IOrchestrator):
            raise TypeError(f"The implemented orchestrator the IOrchestrator interface.")

    def __check_environment(self):
        if not isinstance(self.environment, IEnvironment):
            raise TypeError(f"The implemented orchestrator the IOrchestrator interface.")

        environment_variables = {
            "AUTH_USERNAME",
            "AUTH_PASSWORD",
            "BIGQUERY_PROJECT",
            "BIGQUERY_DATASET",
            "SF_API_HOST",
            "SF_API_USER",
            "SF_API_PASS",
        }
        self.environment.set_environment_variables(environment_variables)
        self.environment.set_configuration_file('./settings.yaml')
        self.environment.check()

    def run(self):
        self.__is_orchestrator()
        self.__check_environment()

        self.orchestrator.set_mapper_manager(GlobalMapperManager())
        self.orchestrator.set_mapper_manager(SapEmployeesMapperManager())

        self.orchestrator.set_input_manager(GlobalInputManager())
        self.orchestrator.set_input_manager(SapEmployeesInputManager())

        self.orchestrator.set_transformer_manager(GlobalTransformerManager())
        self.orchestrator.set_transformer_manager(SapEmployeesTransformerManager())

        self.orchestrator.set_output_manager(GlobalOutputManager())
        self.orchestrator.set_output_manager(SapEmployeesOutputManager())

        self.orchestrator.run()

    def get_version(self):
        return self.environment.get_value("VERSION")

    def get_summary(self):
        return self.orchestrator.get_summary()
