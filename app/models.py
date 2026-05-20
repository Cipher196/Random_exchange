from app import db
from flask_login import UserMixin
from app import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(20), unique=True, nullable=False)
    email=db.Column(db.String(50), unique=True, nullable=False)
    password=db.Column(db.String(200), nullable=False)
    questions=db.relationship('Question', backref='author', lazy=True)
    answers=db.relationship('Answer', backref='author', lazy=True)

    def __repr__(self):
        return f"User('{self.username}','{self.email}')"


class Question(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(30), nullable=False)
    question=db.Column(db.Text, nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class Answer(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    # title=db.Column(db.String(30), nullable=False)
    answer=db.Column(db.Text, nullable=False)
    user_id=db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    question_id=db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    created_at=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)




