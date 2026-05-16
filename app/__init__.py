from flask import Flask
from .extensions import db
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

bcrypt=Bcrypt()
login_manager=LoginManager()

def create_app():
    app = Flask(__name__)

    app.config.from_object("config.Config")

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    from .routes import main
    app.register_blueprint(main)

    return app
