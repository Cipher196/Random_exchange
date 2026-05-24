import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = '6c4796e072f0630f8cba09f44f53239c'

    uri = os.getenv("DATABASE_URL")

    if uri:
        if uri.startswith("postgres://"):
            uri = uri.replace("postgres://", "postgresql://", 1)
    else:
        uri = "sqlite:///" + os.path.join(basedir, "site.db")

    SQLALCHEMY_DATABASE_URI = uri
    SQLALCHEMY_TRACK_MODIFICATIONS = False
