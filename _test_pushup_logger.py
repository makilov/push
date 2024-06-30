from flask import Flask
from flask_sqlalchemy import SQLAlchemy

import os


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    print(os.getcwd())
    app.config['SECRET_KEY'] = 'secret-key'
    # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/muzo/pushup_logger/instance/db.sqlite'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///instance/db.sqlite'

    print(app.config['SQLALCHEMY_DATABASE_URI'])

    db.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    return app