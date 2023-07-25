import json


def load_config(file_path):
    with open(file_path, 'r') as file:
        config_data = json.load(file)
    return config_data

config = load_config('../conf/config.json')

unet_model_location = config["unet_model_location"]
dallE_api_key = config["dallE_api_key"]