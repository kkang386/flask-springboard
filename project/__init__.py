import os
import sys
import config
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from project.envs import Envs
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with


envs = Envs('config')
# sys.argv[1] won't work if pytest runner want to run a specific test file.
# configClass = envs.get_env(sys.argv[1]) if len(sys.argv) == 2 else envs.get_env( os.environ["ENV_NAME"] )
configClass = envs.get_env(os.environ["ENV_NAME"])
app = Flask(__name__)
app.config.from_object(configClass)
api = Api(app)

# db.init_app(app)
db = SQLAlchemy(app)

#from project.models import User, VideoModel
from project.routes import configure_routes, configure_api_routes

configure_routes(app)
configure_api_routes(api)
