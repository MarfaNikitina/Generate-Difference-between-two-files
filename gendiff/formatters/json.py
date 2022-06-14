import json


def render(diff_dict):
    result = json.dumps(diff_dict, indent=4)
    return result
