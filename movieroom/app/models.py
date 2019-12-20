from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

from .extensions import encrypt, login_manager

db = SQLAlchemy()


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(db.Model):
    __tablename__ = 'Users'

    id = db.Column(db.Integer,
                   primary_key=True)

    fname = db.Column(db.String(80))

    lname = db.Column(db.String(80))

    email = db.Column(db.String(80),
                      unique=True,
                      nullable=False)

    uname = db.Column(db.String(80),
                      unique=True,
                      nullable=False)

    pword = db.Column(db.String(80),
                      nullable=False)

    created_on = db.Column(db.DateTime,
                           nullable=False)

    is_admin = db.Column(db.Boolean,
                         default=False,
                         nullable=False)

    def __init__(self, uname, pword, email,
                 fname=None, lname=None, is_admin=False):
        self.fname = fname
        self.lname = lname
        self.email = email
        self.uname = uname
        self.pword = encrypt(pword)
        self.created_on = datetime.now()
        self.is_admin = is_admin

    def __repr__(self):
        return f'User: {self.uname} <{self.email}> created on \
                 {str(self.created_on)}'

    def pwordCheck(self, given):
        return encrypt(given) == self.pword

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id
