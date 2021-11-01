import os

from flask import Flask, Blueprint, render_template, request
from functions import allowed_file, img_to_base64, add_to_db, connect

main = Blueprint('main', __name__)


@main.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        f = request.files.get('file')
        path_to_save = os.path.join('S:\\Zivju_projeketelis\\', f.filename)
        f.save(path_to_save)
        bilde = img_to_base64(path_to_save)
        add_to_db(1, bilde, 1, '31.10.2021', 1)

    connect.open_connection()
    connect.cur.execute("SELECT Bilde FROM Loms WHERE Lietotaja_ID == 1")
    oi = [r[0] for r in connect.cur]
    connect.close_connection()
    return render_template('index.html', photos=oi)
