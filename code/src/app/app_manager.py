from src.app.input.global_input_manager import GlobalInputManager
from src.app.mapper.global_mapper_manager import GlobalMapperManager
from src.app.orchestrator.orchestrator import Orchestrator
from src.app.output.global_output_manager import GlobalOutputManager
from src.app.transformer.first_transformer_manager import (
    FirstTransformerManager,
)
from src.core.app_manager_interface import IAppManager
from src.core.environment.environment import Environment
from src.core.environment.environment_interface import IEnvironment
from src.core.orchestrator.orchestrator_interface import IOrchestrator

# Set the list of enviroment variables for the project
ENVIRONMENT_VARIABLES = []


class AppManager(IAppManager):
    """
    Application manager
    Entry point of the application, here the different pipelines that the
    application has are defined.
    """

    def __init__(self):
        self.orchestrator = Orchestrator()
        self.environment = Environment()
        self.__initialize_environment_variables()

        if not isinstance(self.orchestrator, IOrchestrator):
            raise TypeError(
                "The implemented orchestrator the IOrchestrator interface."
            )

    def __initialize_environment_variables(self):
        if not isinstance(self.environment, IEnvironment):
            raise TypeError(
                "The implemented orchestrator the IOrchestrator interface."
            )

        self.environment.set_environment_variables(ENVIRONMENT_VARIABLES)
        self.environment.set_configuration_file("./settings.yaml")
        self.environment.check()

    def run(self):
        self.orchestrator.set_mapper_manager(GlobalMapperManager())

        self.orchestrator.set_input_manager(GlobalInputManager())

        self.orchestrator.set_transformer_manager(FirstTransformerManager())

        self.orchestrator.set_output_manager(GlobalOutputManager())

        self.orchestrator.run()

    def get_version(self):
        return self.environment.get_value("VERSION")

    def get_summary(self):
        return self.orchestrator.get_summary()
