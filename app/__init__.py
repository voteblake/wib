from flask import Flask
from flask.ext.bootstrap import Bootstrap
from config import config

from flask_flatpages import FlatPages

pages = FlatPages()
bootstrap = Bootstrap()

def create_app(config_name):
    """
    Wrapper function to initialize dependencies and return
    callable Flask app object to WSGI server.
    """
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    pages.init_app(app)
    bootstrap.init_app(app)

    from .blog import blog as blog_blueprint
    app.register_blueprint(blog_blueprint)

    import logging
    from logging import FileHandler

    file_handler = FileHandler('error.log')
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)

    return app
