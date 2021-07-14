from webapp.board.forms import BoardForm
from webapp.board.models import Board
from webapp.notice.models import Notice
from flask import Blueprint, render_template, current_app, redirect, flash, abort
from flask.helpers import url_for
from flask_login import login_required, current_user
from webapp.db import db
from datetime import datetime



blueprint = Blueprint('board', __name__, url_prefix='/boards')

@blueprint.route('/')
def all_boards():
    title = 'Список всех досок'
    all_boards = Board.query.all()
    return render_template ('boards/all_boards.html', boards=all_boards)


@blueprint.route('/ar/<int:board_id>')
def board_ar(board_id):
    title = "AR"
    all_notices = Notice.query.filter(Notice.board_id == board_id).all()
    all_notices_str = str(" ")
    all_notices_str = all_notices_str.join(all_notices)
    
    return render_template('boards/ar1.html', notices = all_notices_str)

@blueprint.route('/<int:board_id>')
def single_board(board_id):
    title = "board"
    single_board = Board.query.filter(Board.board_id == board_id).first()
    all_notices = Notice.query.filter(Notice.board_id == board_id).all()
    if not single_board:
        abort(404)
        
    #notice_form=NoticeForm()
    return render_template('boards/single_board.html', board=single_board, notices = all_notices)
    #url = url_for('board.board', _external = True)
    #return render_template('boards/board.html', page_title=title)

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
            return redirect(url_for('index')) #исправить на notices.<<int:notice_id>>
        flash('Пожалуйста, исправьте ошибки')
        return redirect(url_for('board.board_add'))
    flash ('Добавлять доски может только admin')
    return redirect(url_for('board.board'))