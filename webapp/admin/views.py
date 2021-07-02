from flask import Blueprint, render_template, current_app
from flask.helpers import url_for
from flask_login import login_required, current_user


blueprint = Blueprint('admin', __name__, url_prefix='/admin')


@blueprint.route('add_board.html')
@login_required
def add_board():
    if current_user.is_admin:
        title = "adding board"
        url = url_for('admin.add_board', _external = True)
        return render_template('admin/add_board.html', page_title=title)
    else:
        return "Добавлять доски может только администратор"