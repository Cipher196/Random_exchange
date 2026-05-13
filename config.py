import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = '6c4796e072f0630f8cba09f44f53239c'
    # This points specifically to your 'instance' directory
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app', 'database/app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
