from flask import flask
from flask_bootstrap import Bootstrap
from config import config_options

bootstrap = Bootstrap()

def create_app(config_name):
    app = Flask(_name_)
    # creating the app configurations
    app.config.from _object(config_options[config_name])
    # initializing flask extensions
    bootstrap.init_app(app)
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)
    # setting configurations
    from .requests import configure_request
    configure_request(app)

    return app