from .extensions import db

class User(db.Model):
    id=db.Column(db.Integer, primarykey=True)
    username=db.Column(db.String(20), unique=True, nullable=False)
    email=db.Column(db.String(50), unique=True, nullable=False)
    password=db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f"User('{self.username}','{self.email}')"

