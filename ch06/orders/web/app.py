from flask import Flask
from flask_smorest import Api

from orders.api.api import blueprint
from orders.config.base import BaseConfig


def create_app():
    app = Flask(__name__)
    app.config.from_object(BaseConfig)

    orders_api = Api(app)

    orders_api.register_blueprint(blueprint)

    return app


app = create_app()
