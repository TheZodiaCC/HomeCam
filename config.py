from access.access_creds import AccessCreds


class Config:
    APP_PORT = 8080
    APP_HOST = "0.0.0.0"
    DEBUG_MODE = False
    APP_TIMEOUT = 300
    CAMERA_ID = AccessCreds.access_details["camera_name"]
    API_TOKEN = AccessCreds.access_details["api_token"]
