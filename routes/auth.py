from flask import render_template, request, redirect, url_for, Blueprint
import flask_login
from access.access import User
from access.access_creds import AccessCreds


auth_ = Blueprint("auth", __name__, template_folder='template', static_folder='static')


@auth_.route("/auth/login")
def login():
    if flask_login.current_user.is_authenticated:
        return redirect(url_for("content.home"))
    else:
        access_account = AccessCreds.access_details
        camera_id = access_account["camera_name"]

        return render_template("login.html", camera_id=camera_id)


@auth_.route("/auth/login/check", methods=["POST"])
def check():
    if flask_login.current_user.is_authenticated:
        return redirect(url_for("content.home"))
    else:
        try:
            access_account = AccessCreds.access_details

            if request.form["password"] == access_account["camera_access_password"]:
                user = User()
                user.id = access_account["camera_name"]

                flask_login.login_user(user)

                return redirect(url_for("content.home"))
            else:
                message = "Wrong password"
                return render_template("login.html", message=message)

        except:
            message = "Wrong password"
            return render_template("login.html", message=message)


@auth_.route("/auth/logout", methods=["POST", "GET"])
@flask_login.login_required
def logout():
    flask_login.logout_user()

    return redirect(url_for("content.home"))
