from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, InputRequired, Length, Email, EqualTo, ValidationError
import sqlite3


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
        Length(min=4, max=16, message="Username must be between {} and {} characters long".format(min, max))])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[
        InputRequired(message='Name must contain text!'),
        Length(min=3, max=20, message="Name must be between {} and {} characters long".format(min, max))
    ])
    username = StringField('Username', validators=[
        InputRequired(message='Username must contain text!'),
        Length(min=4, max=16, message="Username must be between {} and {} characters long".format(min, max))
    ])
    password = PasswordField('Password', validators=[
        InputRequired(),
        EqualTo('confirm', message='Passwords must match'),
        Length(min=4, max=16, message="Password must be between {} and {} characters long".format(min, max))
    ])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField('Sign up')
