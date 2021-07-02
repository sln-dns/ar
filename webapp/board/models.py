from webapp.db import db



class Board(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String, nullable=False)
        board = db.Column(db.String, unique=True, nullable=False)
        date = db.Column(db.DateTime, nullable=False)
        text = db.Column(db.Text, nullable=True)
        author = db.Column(db.Text, nullable=True)
        

        def __repr__(self):
            return '<Board {} {}>'.format(self.title, self.url)