from src.core.app_manager_interface import IAppManager
from src.core.orchestrator.orchestrator_interface import IOrchestrator
from src.core.environment.environment_interface import IEnvironment
from src.core.environment.environment import Environment
from src.app.orchestrator.orchestrator import Orchestrator

from src.app.mapper.global_mapper_manager import GlobalMapperManager

from src.app.input.global_input_manager import GlobalInputManager

from src.app.transformer.global_transformer_manager import GlobalTransformerManager

from src.app.output.global_output_manager import GlobalOutputManager

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

        environment_variables = []
        self.environment.set_environment_variables(environment_variables)
        self.environment.set_configuration_file('./settings.yaml')
        self.environment.check()

    def run(self):
        self.__is_orchestrator()
        self.__check_environment()

        self.orchestrator.set_mapper_manager(GlobalMapperManager())

        self.orchestrator.set_input_manager(GlobalInputManager())

        self.orchestrator.set_transformer_manager(GlobalTransformerManager())

        self.orchestrator.set_output_manager(GlobalOutputManager())

        self.orchestrator.run()

    def get_version(self):
        return self.environment.get_value("VERSION")

    def get_summary(self):
        return self.orchestrator.get_summary()
