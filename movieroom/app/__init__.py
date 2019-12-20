from flask import Flask, render_template

from .extensions import database_ready


def create_app():
    app = Flask(__name__, instance_relative_config=False,
                template_folder='templates',
                static_folder='static')
    app.config.from_object('config.Config')

    with app.app_context():

        from .extensions import db
        db.init_app(app)

        if database_ready(db, app):
            db.create_all()
            db.session.commit()

        @app.route('/')
        def index():
            return render_template('index.html',
                                   title="Movie Room")

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
