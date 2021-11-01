from flask import Flask, render_template, request, url_for
from flask_dropzone import Dropzone
from views import main

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)
    UPLOAD_FOLDER = 'S:\\Zivju_projeketelis\\'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    dropzone = Dropzone(app)
    app.config['DROPZONE_MAX_FILE_SIZE'] = 10
    app.config['DROPZONE_REDIRECT_VIEW'] = 'main.hello_world'
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0',port=8000)
