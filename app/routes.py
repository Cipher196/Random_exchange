from flask import Blueprint, render_template, request, redirect, flash, url_for
from app.forms import RegistrationForm

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
        print("validation success")
        flash('Thank for registration!')
        return redirect(url_for('main.login'))
    return render_template('register.html', form=form)


@main.route('/login', methods=['GET','POST'])
def login():
    form=LoginForm()
    if request.method=='POST' and form.validate():
        flash('Thank for Login!')
        return redirect(url_for(main.about_project))
    return render_template('login.html', form=form)

