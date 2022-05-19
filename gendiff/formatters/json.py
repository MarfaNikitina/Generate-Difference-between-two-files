# !/usr/bin/env python3
import json


def make_json_format(diff_dict):
    result = json.dumps(diff_dict, indent=4)
    return result
