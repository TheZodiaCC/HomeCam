import json
import os


class AccessCreds:
    current_dir = os.path.dirname(os.path.realpath(__file__))

    with open(os.path.join(current_dir, "creds.json"), "r") as creds:
        access_details = json.loads(creds.read())
