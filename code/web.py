from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint
from flask_restful import  Api
from flask_swagger import swagger

from src.app.app_manager import AppManager
from src.core.helper.logger import Logger
from src.core.exception.abort_process_exception import AbortProcessException
from src.core.exception.no_data_to_process_exception import NoDataToProcessException
from src.app.views.version import VersionView


app = Flask(__name__)
api = Api(app)

SWAGGER_URL = '/swagger'
API_URL = '/swagger.json'

swagger_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Tiber framework API"
    }
)

app.register_blueprint(swagger_blueprint, url_prefix=SWAGGER_URL)

@app.route('/swagger.json')
def spec():
    swag = swagger(app)
    swag['info']['version'] = "1.0"
    swag['info']['title'] = "Tiber framework API"

    return swag

api.add_resource(VersionView, '/version')


# @app.route('/finance-data', methods=(['GET']))
# def finance_data():
#     logger = Logger()
#     app_manager = AppManager()
#     try:
#         logger.info(f"Process started.")
#         app_manager.run()
#         return jsonify({"response": app_manager.get_summary()}), 200
#     except NoDataToProcessException as err:
#         logger.info(str(err))
#         return jsonify(), 204
#     except AbortProcessException as err:
#         logger.critical(str(err), True)
#         return jsonify({"response": "KO", "error_message": str(err)}), 500
#     except Exception as err:
#         logger.error(str(err), True)
#         return jsonify({"response": "KO", "error_message": str(err)}), 500

# @app.route('/version', methods=(['GET']))
# def version():
#     app_manager = AppManager()

#     return jsonify({ "response": app_manager.get_version() }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0')
