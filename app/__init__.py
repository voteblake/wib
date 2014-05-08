from flask import Flask
from config import config

from flask_flatpages import FlatPages

pages = FlatPages()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    pages.init_app(app)

    from .blog import blog as blog_blueprint
    app.register_blueprint(blog_blueprint)

    return app
