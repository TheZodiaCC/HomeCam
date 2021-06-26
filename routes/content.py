from flask import render_template, Blueprint, redirect, url_for
import flask_login

content_ = Blueprint("content", __name__, template_folder='template', static_folder='static')


@content_.route("/")
def home():
    if flask_login.current_user.is_authenticated:
        return render_template("index.html")
    else:
        return redirect(url_for("auth.login"))
