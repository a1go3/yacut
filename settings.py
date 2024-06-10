import os

URL = 'http://localhost/'
REGEX = r'[A-Za-z0-9_]+$'
MAX_LENGTH_SHORT_URL = 16


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SECRET_KEY = os.getenv('SECRET_KEY')
    STATIC_URL_PATH = ''
    STATIC_FOLDER = '../html/'
    TEMPLATE_FOLDER = '../html/templates'
