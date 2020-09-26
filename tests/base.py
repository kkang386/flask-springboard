# run: python -m unittest discover
import unittest

from project import app, db
from project.models import User, VideoModel 


class BaseTestCase(unittest.TestCase):
    """A base test case."""

    def create_app(self):
        app.config.from_object('config.TestingConfig')
        return app
"""
    def setUp(self):
        db.create_all()
        db.session.add(User("admin", "ad@min.com", "admin"))
        db.session.add(
            BlogPost("Test post", "This is a test. Only a test.", "admin"))
        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
"""
