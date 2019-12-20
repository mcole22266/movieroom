from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Length


class LoginForm(FlaskForm):

    uname = StringField('Username', validators=[
        InputRequired(),
        Length(max=80, message='Field too long')
    ])

    pword = PasswordField('Password', validators=[
        InputRequired()
    ])

    submit = SubmitField('Log In')
