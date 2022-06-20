import json
import yaml


def parse(data, format):
    if format == ".json":
        return json.load(data)
    elif format == '.yaml' or format == '.yml':
        return yaml.safe_load(data)
    raise Exception(f'Format {format} is not supported by the program.')
