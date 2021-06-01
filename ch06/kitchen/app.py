from flask import Flask
from flask_smorest import Api

from api.api import blueprint
from config import BaseConfig


app = Flask(__name__)
app.config.from_object(BaseConfig)

kitchen_api = Api(app)

kitchen_api.register_blueprint(blueprint)
