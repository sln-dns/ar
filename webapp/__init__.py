from flask import Flask, render_template, request, send_from_directory, flash, redirect
from webapp.user.forms import LoginForm
from flask.helpers import url_for
from flask_migrate import Migrate
from webapp.db import db
from webapp.user.models import User
from webapp.board.models import Board
from webapp.notice.models import Notice
from flask_login import LoginManager, login_user, current_user, logout_user, login_required
from webapp.user.views import blueprint as user_blueprint
from webapp.board.views import blueprint as board_blueprint
from webapp.notice.views import blueprint as notice_blueprint
from webapp.admin.views import blueprint as admin_blueprint


#from coordinates import longitude_now, latitude_now


def create_app():
    app = Flask(__name__, static_folder='static', static_url_path='')
    app.config.from_pyfile('config.py')
    db.init_app(app)
    migrate = Migrate(app, db, render_as_batch=True)
    
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(user_blueprint)
    app.register_blueprint(board_blueprint)
    app.register_blueprint(notice_blueprint)
    app.register_blueprint(admin_blueprint)


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
        return render_template('boards/index.html', page_title=title)

    
    
    return app