import json
import os


def read_creds():
    current_dir = os.path.dirname(os.path.realpath(__file__))
    path_to_creds = os.path.join(current_dir, os.path.join("access", "creds.json"))

    with open(path_to_creds, "r") as creds:
        creds_data = json.loads(creds.read())

    return creds_data


def save_creds(creds_data):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    path_to_creds = os.path.join(current_dir, os.path.join("access", "creds.json"))

    with open(path_to_creds, "w") as creds:
        creds.write(json.dumps(creds_data, indent=4))


def save_key(api_key):
    creds_data = read_creds()

    creds_data["api_token"] = api_key

    save_creds(creds_data)


def load_api_key():
    creds = read_creds()

    return creds["api_token"]
