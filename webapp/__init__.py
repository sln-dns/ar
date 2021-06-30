from flask import Flask, render_template, request, send_from_directory, flash, redirect
from webapp.forms import LoginForm
from flask.helpers import url_for
from webapp.models import db, Board, Notice, User
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
#from coordinates import longitude_now, latitude_now


def create_app():
    app = Flask(__name__, static_folder='static', static_url_path='')
    app.config.from_pyfile('config.py')
    db.init_app(app)
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)


    @app.route('/static/<path:path>')
    def send_js(path):
        return send_from_directory('/static', path)

    @app.route('/')
    def index():
        title = "list of boards"
            #    longitude = longitude_now()
            #    latitude = latitude_now()
        return render_template('index.html', page_title=title)

    @app.route('/templates/board.html')
    def board():
        title = "board"
        url = url_for('board', _external = True)
        return render_template('board.html', page_title=title)

    @app.route('/templates/message.html')
    def message():
        title = "message"
        url = url_for('message', _external = True)
        return render_template('message.html', page_title=title)

    @app.route('/templates/add_board.html')
    @login_required
    def add_board():
        if current_user.is_admin:
            title = "adding board"
            url = url_for('add_board', _external = True)
            return render_template('add_board.html', page_title=title)
        else:
            return "Добавлять доски может только администратор"

    @app.route('/login')
    
    def login():
        if current_user.is_authenticated:
            return redirect(url_for('index'))
        title = 'Авторизация'
        login_form = LoginForm()
        return render_template('login.html', page_title = title, form = login_form)


    @app.route('/process-login', methods=['POST'])
    def process_login():
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            if user and user.check_password(form.password.data):
                login_user(user)
                flash('Вы вошли на сайт')
                return redirect(url_for('index'))
        flash('Неправильное имя пользователя или пароль')
        return redirect(url_for('login'))

    @app.route('/logout')
    def logout():
        logout_user()
        flash('Вы успешно разлогинились')
        return redirect(url_for('index'))    

    return app