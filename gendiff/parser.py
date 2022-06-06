import json
import yaml


def load_file_by_format(file):
    if file.endswith(".json"):
        loaded_file = json.load(open(f'{file}'))
    elif file.endswith(".yml") or file.endswith(".yaml"):
        loaded_file = yaml.safe_load(open(f'{file}'))
    return loaded_file