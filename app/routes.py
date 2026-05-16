from flask import Blueprint, render_template, request, redirect, flash, url_for
from app.forms import RegistrationForm, LoginForm
from app import bcrypt, db
from app.models import User
from flask_login import login_user, current_user, logout_user

main = Blueprint("main", __name__)

@main.route('/')
def home():
    return render_template("index.html")

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
        user=User(username=form.username.data, password=pw_hash, email=form.email.data)
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
            flash('Thank for Login!','success')
            return redirect(url_for('main.home'))
        else:
            flash('Data incorrect!!', 'danger')

    else:
        if request.method=='POST':
            print(form.errors)
            flash('Login unsuccessfull', 'danger')
    return render_template('login.html', form=form)


@main.route('/logout')
def logout():
    logout_user()
    flash('Successful logout', 'success')
    return redirect(url_for('main.home'))
