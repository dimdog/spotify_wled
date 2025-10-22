import json

def get_config():
    with open("config.json", "r") as configfile:
        config = json.load(configfile)
    return config