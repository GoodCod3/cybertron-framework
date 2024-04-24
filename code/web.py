from flask import Flask
from flask_restful import Api
from flask_swagger import swagger
from flask_swagger_ui import get_swaggerui_blueprint
from src.app.resources.first_entry.main import MainRoute
from src.app.resources.version import VersionView

app = Flask(__name__)
api = Api(app)

SWAGGER_URL = "/swagger"
API_URL = "/swagger.json"

swagger_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Tiber framework API"}
)

app.register_blueprint(swagger_blueprint, url_prefix=SWAGGER_URL)


@app.route("/swagger.json")
def spec():
    swag = swagger(app)
    swag["info"]["version"] = "1.0"
    swag["info"]["title"] = "Tiber framework API"

    return swag


api.add_resource(MainRoute, "/")
api.add_resource(VersionView, "/version")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
