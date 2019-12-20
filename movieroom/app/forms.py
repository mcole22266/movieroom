from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import (InputRequired, Length, Email,
                                Optional, ValidationError, EqualTo
                                )

from .models import User


def usernameTaken(form, field):
    if User.query.filter_by(uname=field.data).first():
        raise ValidationError('That username is already taken.')


def emailAlreadyExists(form, field):
    if User.query.filter_by(email=field.data).first():
        raise ValidationError('There is already an account associated with \
                              this address.')


class LoginForm(FlaskForm):

    uname = StringField('Username', validators=[
        InputRequired(),
        Length(max=80, message='Field too long')
    ])

    pword = PasswordField('Password', validators=[
        InputRequired()
    ])

    submit = SubmitField('Log In')


class CreateAccountForm(FlaskForm):

    fname = StringField('First Name', validators=[
        Length(max=80,
               message='First Name cannot be longer than 50 characters'),
        Optional()
    ],  render_kw={"placeholder": "Optional"})

    lname = StringField('Last Name', validators=[
        Length(max=80,
               message='Last Name cannot be longer than 50 characters'),
        Optional()
    ],  render_kw={"placeholder": "Optional"})

    email = StringField('Email', validators=[
        InputRequired(message="An email is required."),
        Length(min=6, max=(80),
               message="Email must be between 6 and 80 characters."),
        Email(message="A valid email is required."),
        emailAlreadyExists
    ])

    uname = StringField('Username', validators=[
        InputRequired(message="You must pick a username."),
        Length(min=6, max=20,
               message='Usernames must be between 6 and 20 characters.'),
        usernameTaken
    ])

    pword = PasswordField('Password', validators=[
        InputRequired(message="You must pick a password."),
        EqualTo('pwordConfirm', message='Your passwords do not match.'),
    ])

    pwordConfirm = PasswordField('Confirm Password', validators=[
        InputRequired(message="You must confirm your password."),
        EqualTo('pword', message='Your passwords do not match.')
    ])

    submit = SubmitField('Create Account')
