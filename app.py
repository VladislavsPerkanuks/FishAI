from flask import render_template, session, url_for, flash, request, redirect, Response
import sqlite3
from flask_login import login_manager, LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from forms import LoginForm, RegisterForm
from passlib.hash import sha256_crypt
import os
from datetime import datetime
from classes import User
from run import create_app
from functions import *
from model.predictions import predict
import pandas as pd

db = 'DAB.db'

app = create_app()
login_manager = LoginManager(app)
login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    conn = sqlite3.connect(db)
    curs = conn.cursor()
    curs.execute("SELECT * from Lietotajs where id = (?)", [user_id])
    lu = curs.fetchone()
    if lu is None:
        return None
    else:
        return User(int(lu[0]), lu[1], lu[2])


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    form = LoginForm()
    if form.validate_on_submit():
        conn = sqlite3.connect(db)
        curs = conn.cursor()
        curs.execute("SELECT * FROM Lietotajs where Lietotaja_vards = (?)", [form.username.data])
        user = list(curs.fetchone())
        Us = load_user(user[0])
        if form.username.data == Us.username and sha256_crypt.verify(form.password.data, Us.password):
            login_user(Us)
            return redirect(url_for('profile'))
        else:
            flash('Login Unsuccessful.')
    return render_template('login.html', title='Login', form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        conn = sqlite3.connect(db)
        curs = conn.cursor()
        username = form.username.data
        password = sha256_crypt.hash(form.password.data)
        curs.execute("INSERT INTO Lietotajs values (Null,?,?)", [username, password])
        curs.close()
        try:
            conn.commit()
            flash('Register successful')
            return redirect(url_for('login'))
        except:
            flash('Register Unsuccessful.')
    return render_template('register.html', title='Register', form=form)


@app.route("/", methods=['GET', 'POST'])
def profile():
    try:
        query = """SELECT * from Loms where Lietotaja_ID = ? ORDER BY Zvejas_datums DESC """
        connection = sqlite3.connect(db)
        cur = connection.cursor()
        result = pd.read_sql(query, connection, params=[current_user.id])
        cur.close()
        connection.close()
        unique_dates = []
        df_array = []
        normal_dat = []
        for reslt in result['Zvejas_datums']:
            if reslt not in unique_dates:
                unique_dates.append(reslt)
                normal_date = datetime.strptime(reslt, '%Y-%m-%d').strftime('%d.%m.%Y')
                normal_dat.append(normal_date)

        for date in unique_dates:
            hey = result[result['Zvejas_datums'] == date]
            df_array.append(hey)

        # print(df_array)

        for array in df_array:
            print(array['Zvejas_datums'].unique())

        return render_template('profile.html', title="Main gallery", id=current_user.id, datumi=normal_dat,
                               info=df_array)

    except:
        return redirect(url_for('login'))


@app.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route("/upload", methods=['GET', 'POST'])
@login_required
def upload():
    if request.method == 'POST':
        path_photo = get_file_path(request.files.get('file'))
        blob_file = img_to_base64(path_photo)
        predictions = predict(path_photo)
        date = get_today_date()

    return render_template('upload.html', blob_photo=blob_file, predictions=predictions, date=date)


@app.route("/save_fish", methods=['GET', 'POST'])
@login_required
def save_fish():
    if request.method == 'POST':
        data = request.form.to_dict()
        connection = sqlite3.connect(db)
        cur = connection.cursor()
        query = """ INSERT INTO Loms VALUES (Null,?,?,?,?,?,?,?,?)"""

        # date = date_string_from_normal_to_db_format(data['date-inp'])

        values_to_insert = (
            current_user.id, data['blob-file'], data['ai_predict'], data['fish_name'], data['date-inp'],
            data['locat-inp'], data['weight-inp'], data['size-inp'])
        cur.execute(query, values_to_insert)
        cur.close()
        connection.commit()
        connection.close()

    return redirect(url_for('profile'))


@app.route("/bilde", methods=['GET', 'POST'])
@login_required
def bilde():
    bild_id = request.args.get('bild_id')
    return render_template('bilde.html',bild_id=bild_id)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True, debug=True)
