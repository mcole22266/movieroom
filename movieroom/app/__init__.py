from flask import Flask, render_template, redirect, request, url_for
from flask_login import current_user, login_required, login_user, logout_user

from .models import User
from .forms import LoginForm
from .extensions import database_ready, login_manager


def create_app():
    app = Flask(__name__, instance_relative_config=False,
                template_folder='templates',
                static_folder='static')
    app.config.from_object('config.Config')

    with app.app_context():

        from .models import db
        db.init_app(app)

        from flask_wtf.csrf import CSRFProtect
        CSRFProtect(app)

        login_manager.init_app(app)

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

        @app.route('/', methods=['GET', 'POST'])
        def index():
            if current_user.is_authenticated:
                return redirect(url_for('home'))
            form = LoginForm()
            return render_template('index.html',
                                   title="Movie Room",
                                   form=form)

        @app.route('/home')
        @login_required
        def home():
            return 'Home'

        @app.route('/about')
        def about():
            return 'About'

        @app.route('/contact')
        def contact():
            return 'Contact'

        @app.route('/login', methods=['GET', 'POST'])
        def login():
            if current_user.is_authenticated:
                return redirect(url_for('home'))
            form = LoginForm()

            # POST
            if form.validate_on_submit():
                uname = request.form.get('uname')
                pword = request.form.get('pword')
                user = User.query.filter_by(uname=uname).first()
                if user and user.pwordCheck(pword):
                    login_user(user)
                    return redirect(url_for('home'))
                else:
                    return redirect(url_for('login'))

            # GET
            return render_template('login.html',
                                   title="Movie Room - Login",
                                   form=form)

        @app.route('/create')
        def create():
            return 'Create'

        @app.route('/logout')
        @login_required
        def logout():
            logout_user()
            return redirect(url_for('index'))

        @app.route('/setup')
        def setup():
            return 'Setup'

        return app
