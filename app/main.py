from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from flask_cors import CORS

from config import Config as config


cors = CORS()


def setup_swagger(app):
    SWAGGER_URL = '/swagger'
    API_URL = '/static/swagger.yaml'
    swagger_bp = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
            'app_name': "Lecture3_Example3"
        }
    )
    app.register_blueprint(swagger_bp, url_prefix=SWAGGER_URL)


def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")
    setup_swagger(app)
   
    from .views import index_bp
    app.register_blueprint(index_bp)

    cors.init_app(app, resources={r"*": {"origins": "*"}})
    return app
