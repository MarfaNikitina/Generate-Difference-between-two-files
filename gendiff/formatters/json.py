import json


def render(diff):
    result = json.dumps(diff, indent=4)
    return result
