from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from settings import Config

app = Flask(
    __name__, static_url_path='',
    template_folder='../html',
    static_folder='../html'
)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import views

with app.app_context():
    db.create_all()
