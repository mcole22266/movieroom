from flask import Flask


def create_app():
    app = Flask(__name__, instance_relative_config=False,
                template_folder='templates',
                static_folder='static')
    app.config.from_object('config.Config')

    with app.app_context():

        @app.route('/')
        def index():
            return 'Hello World - this is the index page'

        return app
