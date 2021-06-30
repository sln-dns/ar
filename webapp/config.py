import os 
from datetime import timedelta

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, '..', 'ar.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = "45674567"

REMEMBER_COOKIE_DURATION = timedelta(days=1)