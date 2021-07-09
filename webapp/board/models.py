from webapp.db import db



class Board(db.Model):
        board_id = db.Column(db.Integer, primary_key=True)
        adress = db.Column(db.String, nullable=False)
        memorys = db.Column(db.String, unique=True, nullable=True)
        date = db.Column(db.DateTime, nullable=True)
        author = db.Column(db.Text, nullable=True)
        

        def __repr__(self):
            return '<Board {} {}>'.format(self.title, self.url)