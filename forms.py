from flask_wtf import FlaskForm
from wtforms import DateField, DecimalField, FloatField, StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, InputRequired, Length, Email, EqualTo, NumberRange, ValidationError, \
    Optional
import sqlite3
from datetime import date


# def validate_username(username):
#     conn = sqlite3.connect('db')
#     curs = conn.cursor()
#     curs.execute("SELECT Username FROM Lietotajs where Username = (?)", [username.data])
#     valemail = curs.fetchone()
#     if valemail is None:
#         raise ValidationError('This Username ID is not registered. Please register before login')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[
        InputRequired(),
        Length(min=4, max=16, message="Username must be between 4 and 16 characters long")])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[
        InputRequired(message='Name must contain text!'),
        Length(min=3, max=20, message="Username must be between 4 and 16 characters long")
    ])
    username = StringField('Username', validators=[
        InputRequired(message='Username must contain text!'),
        Length(min=4, max=16, message="Username must be between 4 and 16 characters long")
    ])
    password = PasswordField('Password', validators=[
        InputRequired(),
        EqualTo('confirm', message='Passwords must match'),
        Length(min=4, max=16, message="Username must be between 4 and 16 characters long")
    ])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Sign up')


class UploadForm(FlaskForm):
    fish_name = StringField('Fish Name', validators=[
        InputRequired(message='Fish name must not be empty!'),
    ])
    date = DateField('Date', default=date.today(), format='%Y-%m-%d', validators=[
        InputRequired(message='Date must not be empty!')
    ])
    size = DecimalField('Size, cm', validators=[
        Optional(),
        NumberRange(min=0, max=1000, message="Size must not exceed 10 m")
    ])
    weight = DecimalField('Weight, kg', validators=[
        Optional(),
        NumberRange(min=0, max=30, message="Weight must not exceed 30 kg")
    ])
    location = StringField('Location', validators=[
        Optional(),
        Length(min=-1, max=40, message="Location must not exceed 40 characters")
    ])
    save = SubmitField('Save')
