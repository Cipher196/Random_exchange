from flask import Blueprint, render_template, request, redirect, flash, url_for
from app.forms import RegistrationForm, LoginForm

main = Blueprint("main", __name__)

@main.route('/')
def home():
    return render_template("index.html")

@main.route('/about_project')
def about_project():
    return render_template("about_project.html")

@main.route('/register', methods=['GET','POST'])
def register():
    form=RegistrationForm()
    if form.validate_on_submit():
        # print("validation successfull")
        flash('Thank for registration!', 'success')
        return redirect(url_for('main.login'))
    else:
        if request.method=='POST':
            print(form.errors)
            flash('Registration unsuccessfull', 'danger')
    return render_template('register.html', form=form)


@main.route('/login', methods=['GET','POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        # print("validation successfull")
        flash('Thank for Login!','success')
        return redirect(url_for('main.home'))
    else:
        if request.method=='POST':
            print(form.errors)
            flash('Login unsuccessfull', 'danger')
    return render_template('login.html', form=form)

