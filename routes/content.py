from flask import render_template, Blueprint, redirect, url_for, request
import flask_login
import api_utils

content_ = Blueprint("content", __name__, template_folder='template', static_folder='static')


@content_.route("/")
def home():
    if flask_login.current_user.is_authenticated:
        return render_template("index.html")
    else:
        return redirect(url_for("auth.login"))


@content_.route("/main/api_key")
@flask_login.login_required
def api_key():
    return render_template("api.html")


@content_.route("/main/api_key/save", methods=["POST", "GET"])
@flask_login.login_required
def api_key_save():
    api_utils.save_key(request.args.get("api-key"))

    return redirect(url_for("content.api_key"))
