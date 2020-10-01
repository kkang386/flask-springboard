import pytest
import json
import os
# override environemt to be 'test' before testing
os.environ["ENV_NAME"] = 'test'
from project import app, db, configClass
from project.models import User, VideoModel
import config

@pytest.yield_fixture(scope='module')
def setup_test_db():
    def _setup_test_db(app):
        if app.config['SQLALCHEMY_DATABASE_URI'] == config.TestingConfig.SQLALCHEMY_DATABASE_URI:
            # always starting with an empty DB
            db.drop_all()
            db.create_all()

        return app

    yield _setup_test_db(app)

    db.session.remove()
    if app.config['SQLALCHEMY_DATABASE_URI'] == config.TestingConfig.SQLALCHEMY_DATABASE_URI:
        db.drop_all()
        #print ("done testing, do db.drop_all() again")
