import os
import sys
import config
from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from project.envs import Envs
from project.routes import configure_routes

envs = Envs('config')
# sys.argv[1] won't work if pytest runner want to run a specific test file.
# configClass = envs.get_env(sys.argv[1]) if len(sys.argv) == 2 else envs.get_env( os.environ["ENV_NAME"] )
configClass = envs.get_env(os.environ["ENV_NAME"])
app = Flask(__name__)
app.config.from_object(configClass)

# db.init_app(app)
db = SQLAlchemy(app)

from project.models import User, VideoModel

configure_routes(app)
