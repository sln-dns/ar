from sqlalchemy.orm import backref, relationship
from webapp.db import db
from datetime import datetime

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
        user_id = db.Column(
                db.Integer,
                db.ForeignKey('user.id', ondelete='CASCADE'),
                index = True
        )
        notice = relationship('Board', backref='notice')
        user = relationship('User', backref='notice')


        def __repr__(self):
            return '<Notice {}>'.format(self.id)