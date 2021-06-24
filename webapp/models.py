from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Notice(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String, nullable=False)
        text = db.Column(db.Text, nullable=True)
        date = db.Column(db.DateTime, nullable=False, default=datetime.now() )
        author = db.Column(db.Text, nullable=False)
        board_id = db.Column(
                db.Integer,
                db.ForeignKey('board.id', ondelete='CASCADE'),
                index = True
        )

        def __repr__(self):
            return '<Notice {} {}>'.format(self.title, self.url)

class Board(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String, nullable=False)
        board = db.Column(db.String, unique=True, nullable=False)
        date = db.Column(db.DateTime, nullable=False)
        text = db.Column(db.Text, nullable=True)
        author = db.Column(db.Text, nullable=True)
        

        def __repr__(self):
            return '<Board {} {}>'.format(self.title, self.url)

