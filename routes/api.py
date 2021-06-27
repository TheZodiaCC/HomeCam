from flask import Blueprint, jsonify, request, Response
import api_utils
from camera import Camera
from config import Config
import cv2


api_ = Blueprint("api", __name__, template_folder='template', static_folder='static')


@api_.route("/api/get_picture", methods=["POST"])
def get_picture():
    api_key = request.headers.get("API-KEY")

    if api_key == api_utils.load_api_key():
        camera = Camera()

        camera.take_picture()
        frame = camera.frame

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, Config.PICTURE_QUALITY])[1].tolist()

        return jsonify(frame)

    else:
        return Response(status=401)
