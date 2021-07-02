from flask import Blueprint, render_template, current_app
from flask.helpers import url_for
from flask_login import login_required, current_user

blueprint = Blueprint('board', __name__, url_prefix='/boards')

@blueprint.route('/detail')
def board():
    title = "board"
    #url = url_for('board.board', _external = True)
    return render_template('boards/board.html', page_title=title)

