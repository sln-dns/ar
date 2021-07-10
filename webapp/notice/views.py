from flask import Blueprint, render_template, current_app, abort, flash, redirect
from flask.helpers import url_for
from webapp.notice.forms import NoticeForm
from flask_login import current_user 
from datetime import datetime
from webapp.db import db
from webapp.notice.models import Notice
from webapp.user.models import User
from requests import session
 
blueprint = Blueprint('message', __name__, url_prefix="/notice")
 
@blueprint.route('/message.html')
def message():
    title = "message"
    #url = url_for('notice.message', _external = True)
    return render_template('notices/message.html', page_title=title)

@blueprint.route('/<int:notice_id>')
def single_notice(notice_id):
    one_notice = Notice.query.filter(notice_id == notice_id).first()

    if not one_notice:
        abort(404)
        
    notice_form=NoticeForm()
    return render_template('notices/single_notice.html', page_title = one_notice.title, 
                    notice=one_notice)


@blueprint.route('/notice-add')
def notice_add():
  
    form = NoticeForm()
    title = "Добавление объявления"
    return render_template('notices/add_notice.html', page_title=title, form=form)


@blueprint.route('/process-notice-add', methods=['POST'])
def process_add():
    form = NoticeForm()
    date = datetime.now()
    if current_user.is_authenticated:
        author = str(current_user)
        user_id = current_user.get_id()
        if form.validate_on_submit():
            new_notice = Notice(
            title=form.notice_title.data, 
            text=form.notice_text.data,
            date = date, 
            author=author,
            board_id=int(1),
            user_id=user_id, 
            )
            db.session.add(new_notice)
            db.session.commit()
            flash('Объявление добавлено.')
            return redirect(url_for('message.single_notice')) #как сюда передать notice_id???
        flash('Пожалуйста, исправьте ошибки')
        return redirect(url_for('message.notice_add'))
    flash ('Пожалуйста войдите в учетную запись')
    return redirect(url_for('user.login'))

