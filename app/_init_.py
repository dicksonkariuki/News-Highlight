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

    return app