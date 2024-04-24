from src.app.resources.orchestrator_base_view import OrchestratorBaseView


class VersionView(OrchestratorBaseView):
    def get(self):
        """
        This view returns the current version of the application.
        ---
        responses:
          200:
            description: Ok
            schema:
              type: string
        """

        return {
            "response": self.environment.get_value("VERSION"),
        }
