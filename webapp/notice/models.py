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

        def __repr__(self):
            return '<Notice {} {}>'.format(self.title, self.url)