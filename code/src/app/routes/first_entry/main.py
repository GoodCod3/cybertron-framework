from flask_restful import Resource

from src.app.routes.first_entry.app_manager import AppManager
from src.core.helper.logger import Logger


class MainRoute(Resource):
    def __init__(self) -> None:
        super().__init__()
        self.logger = Logger()
        self.app_manager = AppManager()
        
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
            self.app_manager.run()
            self.logger.info("Process started.")

            response_content = {"response": self.app_manager.get_summary()}
        except Exception as err:
            self.logger.error(str(err), from_exception=True)

            response_status = 500
            response_content = {"response": "KO", "error_message": str(err)}

        return response_content, response_status
