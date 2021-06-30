from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

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

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

    @property
    def is_admin(self):
        return self.role == 'admin'

    def __repr__(self):
        return '<User {}>'.format(self.username)
