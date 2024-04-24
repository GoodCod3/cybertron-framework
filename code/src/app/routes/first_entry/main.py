from flask_restful import Resource
from src.app.routes.first_entry.input.first_input_manager import (
    FirstInputManager,
)
from src.app.routes.first_entry.mapper.first_mapper_manager import (
    FirstMapperManager,
)
from src.app.routes.first_entry.output.first_output_manager import (
    FirstOutputManager,
)
from src.app.routes.first_entry.transformer.first_transformer_manager import (
    FirstTransformerManager,
)
from src.core.environment.environment import Environment
from src.core.environment.environment_interface import IEnvironment
from src.core.helper.logger import Logger
from src.core.orchestrator.orchestrator_interface import IOrchestrator

# from src.app.routes.first_entry.orchestrator.orchestrator import Orchestrator
from src.core.orchestrator.types.synchronous import Orchestrator

# Set the list of enviroment variables for the project
ENVIRONMENT_VARIABLES = []


class MainRoute(Resource):
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

    def get(self):
        """
        This is a basic view, it will have to be renamed to adjust it to
        each project and implement the pipeline.
        ---
        responses:
          200:
            description: Ok
            schema:
              type: string
        """
        response_status = 200

        try:
            self.logger.info("Process started.")
            self.orchestrator.set_input_manager(FirstInputManager())

            self.orchestrator.set_transformer_manager(
                FirstTransformerManager()
            )

            self.orchestrator.set_mapper_manager(FirstMapperManager())

            self.orchestrator.set_output_manager(FirstOutputManager())

            self.orchestrator.run()

            response_content = {
                "response": self.orchestrator.get_summary(),
            }
        except Exception as err:
            self.logger.error(str(err), from_exception=True)

            response_status = 500
            response_content = {"response": "KO", "error_message": str(err)}

        return response_content, response_status
