import pytest
import json
import os
# override environemt to be 'test' before testing
os.environ["ENV_NAME"] = 'test'
from project import app, db, configClass
from project.models import User, VideoModel
import config

@pytest.yield_fixture
def setup_test_db():
    def _setup_test_db(app):
        # print ("configClass:", configClass, type(configClass))
        if app.config['SQLALCHEMY_DATABASE_URI'] == config.TestingConfig.SQLALCHEMY_DATABASE_URI:
            print ("do db.drop_all()")
            # always starting with an empty DB
            db.drop_all()
            db.create_all()

        return app

    yield _setup_test_db(app)

    db.session.remove()
    if app.config['SQLALCHEMY_DATABASE_URI'] == config.TestingConfig.SQLALCHEMY_DATABASE_URI:
        db.drop_all()
        #print ("done testing, do db.drop_all() again")
