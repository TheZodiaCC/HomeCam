from access.access_creds import AccessCreds
import os


class Config:
    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    APP_PORT = 8080
    APP_HOST = "0.0.0.0"
    DEBUG_MODE = False
    APP_TIMEOUT = 300
    CAMERA_ID = AccessCreds.access_details["camera_name"]
    API_TOKEN = AccessCreds.access_details["api_token"]

    PREVIEW_CAMERA_WIDTH = 720
    PREVIEW_CAMERA_HEIGHT = 480
    PREVIEW_CAMERA_FPS = 30

    PICTURE_CAMERA_WIDTH = 3280
    PICTURE_CAMERA_HEIGHT = 2464
    PICTURE_QUALITY = 100

    VIDEO_CAMERA_WIDTH = 1920
    VIDEO_CAMERA_HEIGHT = 1080
    VIDEO_CAMERA_FPS = 30

    RECORDINGS_PATH = os.path.join(CURRENT_DIR, "recs")
