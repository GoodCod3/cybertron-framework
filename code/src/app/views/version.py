from flask import jsonify
from flask_restful import Resource

from src.app.app_manager import AppManager


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

        return jsonify({"response": app_manager.get_version()}), 200
