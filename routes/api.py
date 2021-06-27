from flask import Blueprint, jsonify, request, Response, send_file
import api_utils
from camera import Camera
from config import Config
import cv2
import os


api_ = Blueprint("api", __name__, template_folder='template', static_folder='static')


@api_.route("/api/get_picture", methods=["POST"])
def get_picture():
    if api_utils.auth(request.headers.get("API-KEY")):
        camera = Camera()

        camera.take_picture()
        frame = camera.frame

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.imencode('.jpg', frame, [cv2.IMWRITE_JPEG_QUALITY, Config.PICTURE_QUALITY])[1].tolist()

        return jsonify(frame)

    else:
        return Response(status=401)


@api_.route("/api/get_video", methods=["POST"])
def get_video():
    if api_utils.auth(request.headers.get("API-KEY")):
        api_utils.clear_recordings()

        camera = Camera()

        timestamp = api_utils.generate_timestamp()
        camera.record_video(int(request.headers.get("REC-LENGTH")), Config.RECORDINGS_PATH, timestamp)
        path_to_recording = os.path.join(Config.RECORDINGS_PATH, f"{timestamp}.mp4")

        if os.path.exists(path_to_recording):
            return send_file(path_to_recording, as_attachment=True)
        else:
            return Response(status=500)
    else:
        return Response(status=401)
