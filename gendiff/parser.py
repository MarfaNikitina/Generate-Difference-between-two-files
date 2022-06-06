import json
import yaml


def parse_data(data, format):
    if format == ".json":
        return json.load(data)
    elif format == '.yaml' or format == '.yml':
        return yaml.safe_load(data)



# def load_file_by_format(file):
    # if file.endswith(".json"):
        # loaded_file = json.load(open(f'{file}'))
    # elif file.endswith(".yml") or file.endswith(".yaml"):
        # loaded_file = yaml.safe_load(open(f'{file}'))
    # return loaded_file
