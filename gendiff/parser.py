import json
import yaml


def parse(data, format):
    if format == ".json":
        return json.load(data)
    elif format == '.yaml' or format == '.yml':
        return yaml.safe_load(data)
    else:
        print('Error. This format is not supported.')
