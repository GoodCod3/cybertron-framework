from src.app.resources.base_view import BaseView


class VersionView(BaseView):
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
