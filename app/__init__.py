import os

from flask import Flask
from config import Config
from flask_restx import Resource, Api

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config)
# app.config.from_object('src.config.DevConfig')

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI

db = SQLAlchemy(app)
migrate = Migrate(app, db)

login = LoginManager(app)

from app import routes, models, colourdle

api = Api(app)

class Ping(Resource):

    def get(self):
        return {
            'status' : 'success',
            'message' : 'pong.'
        }

api.add_resource(Ping, '/ping')

