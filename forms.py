from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    username = StringField('username',
     validators=[DataRequired()])
    password = PasswordField('password',
        validators=[DataRequired()])

class RegisterForm(FlaskForm):
    username = StringField('username',
     validators=[DataRequired()])
    email = StringField('username',
        validators=[DataRequired(), Email()])
    password = PasswordField('password',
        validators=[DataRequired()])
