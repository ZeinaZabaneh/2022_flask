import os
basedir = os.path.abspath(os.path.dirname(__file__))

class BaseConfig:
    TESTING=false

class DevConfig(BaseConfig):
    pass

class TestConfig(BaseConfig):
    TESTING = True

class ProdConfig(BaseConfig):
    pass

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
