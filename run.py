from flask import Blueprint, Flask
from flask_login import LoginManager


def create_app():
    app = Flask(__name__)
    app.debug = True
    app.secret_key = '444f44fe4fe1fe19f49ef41ef1258'
    login_manager = LoginManager(app)
    login_manager.login_view = "login"
    UPLOAD_FOLDER = 'S:\\Zivju_projeketelis\\'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    return app



