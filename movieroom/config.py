from os import urandom, environ


class Config:

    # app config
    SECRET_KEY = urandom(16)
    FLASK_APP = environ['FLASK_APP']
    FLASK_ENV = environ['FLASK_ENV']
    FLASK_DEBUG = environ['FLASK_DEBUG']
    FLASK_HOST = environ['FLASK_HOST']
    FLASK_PORT = environ['FLASK_PORT']
