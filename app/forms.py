from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from app.models import User

class RegistrationForm(FlaskForm):
    username=StringField('User Name', validators=[DataRequired(), Length(min=3, max=20)])
    email=StringField('Email', validators=[DataRequired(), Email()])
    password=PasswordField('Password', validators=[DataRequired()])
    confirm=PasswordField('Confirm Password', validators=[DataRequired(),EqualTo('password')])
    submit=SubmitField('Sign Up')

    def validate_username(self, username):
        user=User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("doublicate username")

    def validate_email(self, email):
        user=User.query.filter_by(email=email.data.lower()).first()
        if user:
            raise ValidationError("doublicate username")



class LoginForm(FlaskForm):
    username=StringField('User Name', validators=[DataRequired(), Length(min=3, max=20)])
    password=PasswordField('Password', validators=[DataRequired()])
    remember=BooleanField('Remember Me')
    submit=SubmitField('Sign Up')

class QuestionForm(FlaskForm):
    title=StringField('Question Title', validators=[DataRequired(), Length(min=3, max=30)])
    question=TextAreaField('Question', validators=[DataRequired()])
    submit=SubmitField('Submit')


class AnswerForm(FlaskForm):
    # title=StringField('Question Title', validators=[DataRequired(), Length(min=3, max=30)])
    answer=TextAreaField('Answer', validators=[DataRequired()])
    submit=SubmitField('Submit')

