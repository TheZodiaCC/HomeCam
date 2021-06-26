import json
import os


def save_key(api_key):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    path_to_creds = os.path.join(current_dir, os.path.join("access", "creds.json"))

    with open(path_to_creds, "r") as creds:
        creds_data = json.loads(creds.read())

    creds_data["api_token"] = api_key

    with open(path_to_creds, "w") as creds:
        creds.write(json.dumps(creds_data, indent=4))


def load_api_key():
    pass
