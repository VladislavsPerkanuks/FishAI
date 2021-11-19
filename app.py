import ast
from flask import render_template, session, url_for, flash, request, redirect, Response, Flask
import sqlite3
from flask_login import login_manager, LoginManager, UserMixin, login_required, login_user, logout_user, current_user
from forms import LoginForm, RegisterForm, UploadForm
from passlib.hash import sha256_crypt

from classes import User
from functions import *
from model.predictions import predict
import pandas as pd

# from run import app

db = 'DAB.db'

app = Flask(__name__)
app.debug = True
app.secret_key = '444f44fe4fe1fe19f49ef41ef1258'
login_manager = LoginManager(app)
login_manager.login_view = "login"


# app = create_app()
# login_manager = LoginManager(app)
# login_manager.login_view = "login"


@login_manager.user_loader
def load_user(user_id):
    conn = sqlite3.connect(db)
    curs = conn.cursor()
    curs.execute("SELECT * from Lietotajs where id = (?)", [user_id])
    lu = curs.fetchone()
    curs.close()
    conn.close()
    if lu is None:
        return None
    else:
        return User(int(lu[0]), lu[1], lu[2], lu[3])


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('profile'))
    form = LoginForm()
    if form.validate_on_submit():
        conn = sqlite3.connect(db)
        curs = conn.cursor()
        curs.execute("SELECT * FROM Lietotajs where Lietotaja_vards = (?)", [form.username.data])
        user = (curs.fetchone())
        if not user:
            flash('This user is not registered!', 'warning')
            return render_template('login.html', title='Login', form=form)
        user = list(user)
        Us = load_user(user[0])
        if form.username.data == Us.username and sha256_crypt.verify(form.password.data, Us.password):
            login_user(Us)
            return redirect(url_for('profile'))
        else:
            flash('Incorrect password', 'warning')
    return render_template('login.html', title='Login', form=form)


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        conn = sqlite3.connect(db)
        curs = conn.cursor()
        name = form.name.data
        username = form.username.data
        password = sha256_crypt.hash(form.password.data)
        curs.execute("SELECT * FROM Lietotajs where Lietotaja_vards = (?)", [form.username.data])
        user = (curs.fetchone())
        if user:
            flash('This user is already registered!', 'warning')
            return render_template('register.html', title='Register', form=form)

        curs.execute("INSERT INTO Lietotajs values (Null,?,?,?)", [name, username, password])
        curs.close()
        conn.commit()
        flash('Register successful', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/logout", methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route("/", methods=['GET', 'POST'])
def profile():
    try:
        query = """SELECT * from Loms where Lietotaja_ID = ? ORDER BY Zvejas_datums DESC,ID DESC """
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
                normal_date = datetime.strptime(reslt, '%Y-%m-%d').strftime('%A, %d %B %Y')
                normal_dat.append(normal_date)

        for date in unique_dates:
            hey = result[result['Zvejas_datums'] == date]
            df_array.append(hey)

        return render_template('profile.html', title="Main gallery", id=current_user.id, datumi=normal_dat,
                               info=df_array)
    except:
        return redirect(url_for('login'))

@app.route("/photo_upload", methods=['GET', 'POST'])
@login_required
def photo_upload():
    if request.method == 'POST':
        path_photo = get_file_path(request.files.get('file'))
        latitude = request.form.get('latitude')
        longitude = request.form.get('longitude')
        # print(latitude,longitude)
        blob_file = img_to_base64(path_photo)
        connection = sqlite3.connect(db)
        cur = connection.cursor()
        query = """ INSERT INTO temp_bilde VALUES (?,?)"""
        values = (blob_file, current_user.id)
        cur.execute(query, values)
        connection.commit()
        cur.close()
        connection.close()

        predictions = predict(path_photo)
        return redirect(url_for('photo_saving', predictions=predictions,latitude = latitude , longitude = longitude))


@app.route("/photo_saving", methods=['GET', 'POST'])
@login_required
def photo_saving():
    connection = sqlite3.connect(db)
    cur = connection.cursor()
    query = """SELECT bilde FROM temp_bilde WHERE liet_id = ?  AND ROWID IN ( SELECT max( ROWID ) FROM temp_bilde );"""
    values = (current_user.id,)
    cur.execute(query, values)
    photo = list(cur.fetchone())[0]
    cur.close()
    connection.close()

    # photo = request.args.get('photo')
    predictions = split_string_to_array(request.args.getlist('predictions'))
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    print(latitude, longitude)
    if latitude and longitude:
        location = get_closest_location(latitude,longitude)
    else:
        location = ''
    print(location)
    form = UploadForm()
    if form.validate_on_submit():
        date = form.date.data.strftime('%Y-%m-%d')
        location = form.location.data
        weight = None if form.weight.data is None else float(form.weight.data)
        size = None if form.size.data is None else float(form.size.data)
        fish_name = form.fish_name.data

        connection = sqlite3.connect(db)
        cur = connection.cursor()
        query = """ INSERT INTO Loms VALUES (Null,?,?,?,?,?,?)"""

        values_to_insert = (
            current_user.id, photo, date, location, weight, size)
        cur.execute(query, values_to_insert)

        query = """ INSERT INTO Prognozes VALUES (Null,last_insert_rowid(),?,?,?,?,?,?,?)"""
        values_for_query = (
            fish_name,
            predictions[0][0], predictions[0][1],
            predictions[1][0], predictions[1][1],
            predictions[2][0], predictions[2][1]
        )
        cur.execute(query, values_for_query)

        query = """DELETE FROM temp_bilde"""
        cur.execute(query)
        cur.close()
        connection.commit()
        connection.close()
        return redirect(url_for('profile'))

    return render_template('upload.html', blob_photo=photo, predictions=predictions, date=get_today_date(),
                           form=form, location = location)


# @app.route("/save_fish", methods=['GET', 'POST'])
# @login_required
# def save_fish():
#     if request.method == 'POST':
#         # connection = sqlite3.connect(db)
#         # cur = connection.cursor()
#         # query = """ INSERT INTO Prognozes VALUES (Null,?,?,?,?,?,?,?)"""
#         # values_for_query = (
#         #     predictions[0][0],
#         #     predictions[0][0],predictions[0][1],
#         #     predictions[1][0],predictions[1][1],
#         #     predictions[2][0],predictions[2][1]
#         # )
#         # cur.execute(query, values_for_query)
#         # cur.close()
#         # connection.commit()
#         # connection.close()
#
#         data = request.form.to_dict()
#
#     return redirect(url_for('profile'))


@app.route("/bilde", methods=['GET', 'POST'])
@login_required
def bilde():
    bild_id = request.args.get('bild_id')
    connection = sqlite3.connect(db)
    cur = connection.cursor()
    # query = """SELECT * from Loms,Prognozes where Loms.Lietotaja_ID = ? AND Loms.ID = ?"""
    query = """select loms.id,loms.lietotaja_id,bilde,zvejas_datums,zvejas_vieta,svars,izmers,lietotaja_nosaukums,
    nosaukums1,procenti1,nosaukums2,procenti2,nosaukums3,procenti3
    from loms,prognozes
    where loms.id = prognozes.id and Lietotaja_ID = ? and loms.id = ?"""
    result = pd.read_sql(query, connection, params=[current_user.id, bild_id])
    cur.close()
    connection.close()

    result['Zvejas_datums'] = pd.to_datetime(result['Zvejas_datums']).dt.strftime('%d.%m.%Y')

    # return result.to_html()
    return render_template('bilde.html', bild_id=bild_id, info=result)


@app.route("/delete_record", methods=['GET', 'POST'])
@login_required
def delete_record():
    bild_id = request.args.get('bild_id')
    connection = sqlite3.connect(db)
    cur = connection.cursor()
    # query = """SELECT * from Loms,Prognozes where Loms.Lietotaja_ID = ? AND Loms.ID = ?"""
    query = """DELETE FROM Loms WHERE Lietotaja_ID = ? AND LOMS.ID = ?"""
    values_for_query = (current_user.id, bild_id)
    cur.execute(query, values_for_query)
    connection.commit()
    cur.close()
    connection.close()
    return redirect(url_for('profile'))


@app.route("/edit_record", methods=['GET', 'POST'])
@login_required
def edit_record():
    bild_id = request.args.get('bild_id')
    form = UploadForm()
    if form.validate_on_submit():
        date = form.date.data.strftime('%Y-%m-%d')
        location = form.location.data
        weight = None if form.weight.data is None else float(form.weight.data)
        size = None if form.size.data is None else float(form.size.data)
        fish_name = form.fish_name.data

        connection = sqlite3.connect(db)
        cur = connection.cursor()
        query = """UPDATE Loms SET Zvejas_datums = ?, Zvejas_vieta = ?,svars = ?,izmers = ? where loms.id = ?
        AND Lietotaja_ID = ?"""
        values_for_query = (date, location, weight, size, bild_id, current_user.id)

        query2 = """UPDATE Prognozes SET Lietotaja_nosaukums = ? WHERE Loma_ID = ? """
        values_for_query2 = (fish_name, bild_id)

        cur.execute(query, values_for_query)
        cur.execute(query2, values_for_query2)
        connection.commit()
        cur.close()
        connection.close()
        return redirect(url_for('bilde', bild_id=bild_id))

    connection = sqlite3.connect(db)
    cur = connection.cursor()
    query = """select loms.id,loms.lietotaja_id,bilde,zvejas_datums,zvejas_vieta,svars,izmers,lietotaja_nosaukums,
    nosaukums1,procenti1,nosaukums2,procenti2,nosaukums3,procenti3
    from loms,prognozes
    where loms.id = prognozes.id and Lietotaja_ID = ? and loms.id = ?"""
    result = pd.read_sql(query, connection, params=[current_user.id, bild_id])
    cur.close()
    connection.close()
    fishes = ['salmon', 'north pike', 'river perch']
    return render_template('edit.html', title='Edit', info=result, form=form, fishes=fishes)


@app.route("/update_db", methods=['GET', 'POST'])
@login_required
def update_db():
    bild_id = request.args.get('bild_id')
    data = request.form.to_dict()

    return redirect(url_for('bilde', bild_id=data['loms_id']))


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,threaded=True, debug=True)
