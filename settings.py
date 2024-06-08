import os

URL = 'http://localhost/'
REGEX = r'[A-Za-z0-9_]+$'


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')