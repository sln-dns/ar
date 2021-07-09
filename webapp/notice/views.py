from flask import Blueprint, render_template, current_app, abort, flash, redirect
from flask.helpers import url_for
from webapp.notice.forms import NoticeForm
from flask_login import current_user 
from datetime import datetime
from webapp.db import db
from webapp.notice.models import Notice
from requests import session
 
blueprint = Blueprint('message', __name__, url_prefix="/notice")
 
@blueprint.route('/message.html')
def message():
    title = "message"
    #url = url_for('notice.message', _external = True)
    return render_template('notices/message.html', page_title=title)

@blueprint.route('/notices/<int:notice_id>')
def single_notice(notice_id):
    one_notice = Notice.query.filter(notice_id == notice_id).first()

    if not one_notice:
        #abort(404)
        print ('abortabortabortabortabortabortabortabortabort')
    notice_form=NoticeForm()
    return render_template('notice/single_notice.html', page_title = one_notice.title, 
                    notice=one_notice)


@blueprint.route('/notice-add')
def notice_add():
  
    form = NoticeForm()
    title = "Добавление объявления"
    return render_template('notices/add_notice.html', page_title=title, form=form)


@blueprint.route('/process-notice-add', methods=['POST'])
def process_add():
    form = NoticeForm()
    if current_user.is_authenticated:
        if form.validate_on_submit():
            new_notice = Notice(
                title=form.notice_title.data, 
                text=form.notice_text.data, 
                author=current_user, 
                user_id=current_user,  #точно так?
                date=datetime.now,
                )
            db.session.add(new_notice)
            db.session.commit()
            flash('Объявление добавлено.')
            return redirect(url_for('message')) #исправить на notices.<<int:notice_id>>
        flash('Пожалуйста, исправьте ошибки')
        return redirect(url_for('message.notice_add'))
    flash ('Пожалуйста войдите в учетную запись')
    return redirect(url_for('user.login'))

