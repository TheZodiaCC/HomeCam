import json
from config import Config


class AccessCreds:
    CURRENT_DIR = Config.CURRENT_DIR

    with open(f"{CURRENT_DIR}/access/creds.json", "r") as creds:
        access_details = json.loads(creds.read())
