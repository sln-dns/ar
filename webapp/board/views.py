from webapp.board.forms import BoardForm
from webapp.board.models import Board
from flask import Blueprint, render_template, current_app, redirect, flash
from flask.helpers import url_for
from flask_login import login_required, current_user
from webapp.db import db
from datetime import datetime



blueprint = Blueprint('board', __name__, url_prefix='/boards')

@blueprint.route('/detail')
def board():
    title = "board"
    
    #url = url_for('board.board', _external = True)
    return render_template('boards/board.html', page_title=title)

@blueprint.route('/board-add')
def board_add():
    form = BoardForm()
    title = "Добавление доски"
    return render_template('boards/add_board.html', page_title=title, form=form) #вопрос про форму в э

@blueprint.route('/process-board-add', methods=['POST'])
def process_add_board():
    form = BoardForm()
    date = datetime.now()
    if current_user.is_admin:
        author = 'admin'
        if form.validate_on_submit():
            new_board = Board(
                adress=form.adress.data, 
                memorys=form.memorys.data, 
                author=author, 
                date=date,
                )
            db.session.add(new_board)
            db.session.commit()
            flash('Новая доска объявлений добавлена.')
            return redirect(url_for('board.board')) #исправить на notices.<<int:notice_id>>
        flash('Пожалуйста, исправьте ошибки')
        return redirect(url_for('board.board_add'))
    flash ('Добавлять доски может только admin')
    return redirect(url_for('board.board'))