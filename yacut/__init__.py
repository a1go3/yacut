from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from settings import Config

app = Flask(
    __name__,
    static_folder=Config.STATIC_FOLDER,
    template_folder=Config.TEMPLATE_FOLDER
)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from . import api_views, error_handlers, views

with app.app_context():
    db.create_all()
