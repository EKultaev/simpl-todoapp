from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_ckeditor import CKEditor

db = SQLAlchemy()

ckeditor = CKEditor()

def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")

    ckeditor.init_app(app)

    db.init_app(app)

    with app.app_context():
        from . import routes

        db.create_all()

        return app