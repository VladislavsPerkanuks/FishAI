from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
import sqlite3


def validate_username(username):
    conn = sqlite3.connect('db')
    curs = conn.cursor()
    curs.execute("SELECT Username FROM Lietotajs where Username = (?)", [username.data])
    valemail = curs.fetchone()
    if valemail is None:
        raise ValidationError('This Username ID is not registered. Please register before login')


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign up')
