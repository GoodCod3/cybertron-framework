from flask_restful import Resource
from src.app.resources.first_entry.app_manager import AppManager


class VersionView(Resource):
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

        app_manager = AppManager()

        return {"response": app_manager.get_version()}
