from enum import unique
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from webapp.db import db


class User(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password = db.Column(db.String(128))
    role = db.Column(db.String(10), index=True)
    email = db.Column(db.String(50), unique=True)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)

    def get_id(self):
        return self.user_id

    @property
    def is_admin(self):
        return self.role == 'admin'

    def __repr__(self):
        return '<User {}>'.format(self.username)


