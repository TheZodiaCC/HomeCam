from flask import Flask
import flask_login
from access.access import User
import os


def create_app():
    app = Flask(__name__, instance_relative_config=False)
    app.secret_key = os.urandom(25)
    app.config.from_object('config.Config')

    login_manager = flask_login.LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def user_loader(camera_id):
        user = User()
        user.id = camera_id

        return user

    with app.app_context():
        from routes import content, auth, errors

        app.register_blueprint(content.content_)
        app.register_blueprint(auth.auth_)
        app.register_blueprint(errors.errors_)

        return app
