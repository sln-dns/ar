from flask import Blueprint, render_template, current_app
from flask.helpers import url_for
 
blueprint = Blueprint('message', __name__, url_prefix="/notice")
 
@blueprint.route('/message.html')
def message():
    title = "message"
    #url = url_for('notice.message', _external = True)
    return render_template('notices/message.html', page_title=title)
