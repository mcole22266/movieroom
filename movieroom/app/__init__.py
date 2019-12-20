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

        @app.route('/about')
        def about():
            return 'About'

        @app.route('/contact')
        def contact():
            return 'Contact'

        @app.route('/login')
        def login():
            return 'Login'

        @app.route('/create')
        def create():
            return 'Create'

        @app.route('/setup')
        def setup():
            return 'Setup'

        return app
