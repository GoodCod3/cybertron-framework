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
        try:
            logger.info("Process started.")
            app_manager.run()

            return jsonify({"response": app_manager.get_summary()}), 200
        except NoDataToProcessException as err:
            logger.info(str(err))

            return jsonify(), 204
        except AbortProcessException as err:
            logger.critical(str(err), True)

            return jsonify({"response": "KO", "error_message": str(err)}), 500
        except Exception as err:
            logger.error(str(err), True)

            return jsonify({"response": "KO", "error_message": str(err)}), 500
