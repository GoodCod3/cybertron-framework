from flask_restful import Resource

from src.core.environment.environment import Environment
from src.core.environment.environment_interface import IEnvironment
from src.core.helper.logger import Logger
from src.core.orchestrator.orchestrator_interface import IOrchestrator
from src.core.orchestrator.types.synchronous import Orchestrator

# Set the list of enviroment variables for the project
ENVIRONMENT_VARIABLES = []


class OrchestratorBaseView(Resource):
    def __init__(self):
        super().__init__()
        self.logger = Logger()
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

