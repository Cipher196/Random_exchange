from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("index.html")

@main.route('/about_project')
def about_project():
    return render_template("about_project.html")
