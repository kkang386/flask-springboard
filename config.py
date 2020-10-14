import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    WHAT_DO_YOU_KNOW = 'DEFAULT'
    SQLALCHEMY_DATABASE_URL = ''
    ENV_NAME=''
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CACHE_TYPE = "simple" # Flask-Caching related configs
    CACHE_DEFAULT_TIMEOUT = 300

class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://python_test:password@192.168.56.101/python_test'
    ENV_NAME='prod'


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://python_test:password@192.168.56.101/python_test'
    ENV_NAME='stg'


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
    WHAT_DO_YOU_KNOW = 'dever'
    SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://python_test:password@192.168.56.101/python_test'
    ENV_NAME='dev'


class TestingConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/test_database.db'
    ENV_NAME='test'

