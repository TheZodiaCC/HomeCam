from flask import render_template, Blueprint, redirect, url_for, request, Response
import flask_login
import api_utils
from camera import Camera


content_ = Blueprint("content", __name__, template_folder='template', static_folder='static')
CAMERA = Camera()


@content_.route("/")
@flask_login.login_required
def home():
    return render_template("index.html")


@content_.route("/main/camera_switch")
@flask_login.login_required
def camera_switch():
    if CAMERA.is_running:
        CAMERA.stop()
    else:
        CAMERA.start()

    return redirect(url_for("content.home"))


@content_.route('/main/preview')
@flask_login.login_required
def preview():
    return Response(CAMERA.preview_generator(), mimetype='multipart/x-mixed-replace; boundary=frame')


@content_.route("/main/api_key")
@flask_login.login_required
def api_key():
    return render_template("api.html")


@content_.route("/main/api_key/save", methods=["POST", "GET"])
@flask_login.login_required
def api_key_save():
    api_utils.save_key(request.args.get("api-key"))

    return redirect(url_for("content.api_key"))
