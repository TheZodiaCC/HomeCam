import json
import os
import datetime
from config import Config


def read_creds():
    path_to_creds = os.path.join(Config.CURRENT_DIR, os.path.join("access", "creds.json"))

    with open(path_to_creds, "r") as creds:
        creds_data = json.loads(creds.read())

    return creds_data


def save_creds(creds_data):
    path_to_creds = os.path.join(Config.CURRENT_DIR, os.path.join("access", "creds.json"))

    with open(path_to_creds, "w") as creds:
        creds.write(json.dumps(creds_data, indent=4))


def save_key(api_key):
    creds_data = read_creds()

    creds_data["api_token"] = api_key

    save_creds(creds_data)


def load_api_key():
    creds = read_creds()

    return creds["api_token"]


def auth(api_key):
    if api_key == load_api_key():
        return True
    else:
        return False


def generate_timestamp():
    return datetime.datetime.timestamp(datetime.datetime.now())


def clear_recordings():
    for file in os.listdir(Config.RECORDINGS_PATH):
        os.remove(os.path.join(Config.RECORDINGS_PATH, file))
