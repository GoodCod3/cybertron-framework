from src.app.resources.first_entry.input.first_input_manager import (
    FirstInputManager,
)
from src.app.resources.first_entry.output.first_output_manager import (
    FirstOutputManager,
)
from src.app.resources.first_entry.transformer.first_transformer_manager import (  # noqa: E501
    FirstTransformerManager,
)
from src.app.resources.orchestrator_base_view import OrchestratorBaseView


class MainRoute(OrchestratorBaseView):
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
