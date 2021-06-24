from flask import Flask, render_template, request, send_from_directory
from flask.helpers import url_for
from webapp.models import db 
#from coordinates import longitude_now, latitude_now


def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    return app

app = Flask(__name__, static_folder='static', static_url_path='')

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

   