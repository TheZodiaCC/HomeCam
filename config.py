import os


class Config:
    CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
    APP_PORT = 8080
    APP_HOST = "0.0.0.0"
    DEBUG_MODE = False
    APP_TIMEOUT = 0