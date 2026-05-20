from flask import Blueprint, render_template, request, redirect, flash, url_for
from app.forms import RegistrationForm, LoginForm, QuestionForm, AnswerForm
from app import bcrypt, db
from app.models import User, Question, Answer
from flask_login import login_user, current_user, logout_user, login_required
from datetime import datetime

main = Blueprint("main", __name__)

@main.route('/')
def home():
    data=Question.query.order_by(Question.created_at.desc()).all()
    return render_template("index.html", data=data, now=datetime.utcnow())

@main.route('/about_project')
def about_project():
    return render_template("about_project.html")

@main.route('/register', methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        flash('You are already logged in', 'success')
        return redirect(url_for('main.home'))

    form=RegistrationForm()

    if form.validate_on_submit():
        pw_hash=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data, password=pw_hash, email=form.email.data.lower())
        db.session.add(user)
        db.session.commit()
        flash('Thank for registration!', 'success')
        return redirect(url_for('main.login'))
    else:
        if request.method=='POST':
            print(form.errors)
            flash('Registration unsuccessfull', 'danger')
    return render_template('register.html', form=form)


@main.route('/login', methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        flash('You are already logged in', 'success')
        return redirect(url_for('main.home'))

    form=LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            flash('Logged in successfully!','success')
            return redirect(url_for('main.home'))
        else:
            flash('Data incorrect!!', 'danger')

    else:
        if request.method=='POST':
            print(form.errors)
            flash('Login unsuccessful', 'danger')
    return render_template('login.html', form=form)


@main.route('/logout')
def logout():
    logout_user()
    flash('Successful logout', 'success')
    return redirect(url_for('main.home'))


@main.route('/ask', methods=['GET','POST'])
@login_required
def ask():

    form=QuestionForm()
    if form.validate_on_submit():
        question=Question(title=form.title.data, question=form.question.data, author=current_user)
        db.session.add(question)
        db.session.commit()
        flash('Question Submitted Successfully', 'success')
        return redirect(url_for('main.home'))
    else:
        if request.method=='POST':
            print(form.errors)
            flash('Title length should be between 3-30 and detail should be provided', 'danger')
    return render_template('ask.html', form=form)



@main.route('/question/<int:id>')
def question(id):
    question_data=Question.query.filter_by(id=id).first()
    answer_data=Answer.query.filter_by(question_id=id).order_by(Answer.created_at.desc()).all()
    return render_template('question.html', question=question_data, answers=answer_data, now=datetime.utcnow())



@main.route('/answer/<int:question_id>', methods=['GET','POST'])
@login_required
def answer(question_id):
    data=Question.query.filter_by(id=question_id).first()
    form=AnswerForm()

    if form.validate_on_submit():
        answer=Answer(answer=form.answer.data, question_id=question_id, author=current_user)
        db.session.add(answer)
        db.session.commit()
        flash('Answer Submitted Successfully', 'success')
        return redirect(url_for('main.home'))
    else:
        if request.method=='POST':
            print(form.errors)
            flash('Some errror happend. Sorry for inconvinince', 'danger')
    return render_template('answer.html', form=form, question=data)






