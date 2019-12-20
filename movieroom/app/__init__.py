from flask import Flask, render_template

from .models import User
from .extensions import database_ready


def create_app():
    app = Flask(__name__, instance_relative_config=False,
                template_folder='templates',
                static_folder='static')
    app.config.from_object('config.Config')

    with app.app_context():

        from .models import db
        db.init_app(app)

        if database_ready(db, app):
            db.create_all()
            if not User.query.filter_by(uname='admin').first():
                adminUser = User('admin', 'adminpass', 'fakeemail@gmail.com',
                                 is_admin=True)
                db.session.add(adminUser)
                app.logger.info('Admin User added to db')

            if not User.query.filter_by(uname='reg').first():
                regUser = User('reg', 'regpass', 'fakeemail2@gmail.com')
                db.session.add(regUser)
                app.logger.info('Reg User added to db')
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
