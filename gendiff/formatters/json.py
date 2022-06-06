# !/usr/bin/env python3
import json


def structure(diff_dict):
    # структурированный вывод
    result = json.dumps(diff_dict, indent=4)
    return result
