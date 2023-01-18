from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.urandom(23)

    from .auth import auth

    app.register_blueprint(auth, url_prefix='/')

    return app
