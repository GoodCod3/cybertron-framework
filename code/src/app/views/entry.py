from flask import jsonify
from flask_restful import Resource
from src.app.app_manager import AppManager
from src.core.exception.abort_process_exception import AbortProcessException
from src.core.exception.no_data_to_process_exception import (
    NoDataToProcessException,
)
from src.core.helper.logger import Logger


class EntryView(Resource):
    def get(self):
        """
        This is a basic view, it will have to be renamed to adjust it to
        each project.
        ---
        responses:
          200:
            description: Ok
            schema:
              type: string
        """

        logger = Logger()
        app_manager = AppManager()
        response_content = {} 
        response_status = 200
        
        app_manager.run()
        # try:
        #     logger.info("Process started.")

        #     response_content = {"response": app_manager.get_summary()}
        # except NoDataToProcessException as err:
        #     logger.info(str(err))
        #     response_status = 204
        # except AbortProcessException as err:
        #     logger.critical(str(err), from_exception=True)
        #     response_status = 500
        #     response_content = {"response": "KO", "error_message": str(err)}
        # except Exception as err:
        #     logger.error(str(err), from_exception=True)
        #     response_status = 500
        #     response_content = {"response": "KO", "error_message": str(err)}

        return response_content, response_status