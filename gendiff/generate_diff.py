# !/usr/bin/env python3
import itertools
import json
import yaml
from gendiff.formatters.stylish import stylish
#from gendiff.formatters.plain import plain


def load_file_by_format(file):
    if file.endswith(".json"):
        loaded_file = json.load(open(f'tests/fixtures/{file}'))
    elif file.endswith(".yml") or file.endswith(".yaml"):
        loaded_file = yaml.safe_load(open(f'tests/fixtures/{file}'))
    return loaded_file


def create_key_set(dict1, dict2):
    sorted_keys_set = sorted(set(dict1.keys()).union(set(dict2.keys())))
    return sorted_keys_set


def calc_diff(dict1, dict2):
    res_dict = {}
    keys = create_key_set(dict1, dict2)
    for key in keys:
        res_dict[key] = make_status_value_for_key(dict1, dict2, key)
    return res_dict


def make_status_value_for_key(dict1, dict2, key):
    if isinstance(dict1.get(key), dict) and isinstance(dict2.get(key), dict):
        return {
            'STATUS': 'HASCHILD',
            'CHILDREN': calc_diff(dict1[key], dict2[key])
        }
    elif dict1.get(key) == dict2.get(key):
        return {
            'STATUS': 'UNCHANGED',
            'VALUE': dict1[key]
        }
    elif key in dict1.keys() and key not in dict2.keys():
        return {
            'STATUS': 'DELETED',
            'VALUE': dict1[key]
        }
    elif key in dict2.keys() and key not in dict1.keys():
        return {
            'STATUS': 'ADDED',
            'VALUE': dict2[key]
        }
    else:
        return {
            'STATUS': 'CHANGED',
            'VALUE1': dict1[key],
            'VALUE2': dict2[key]
        }


def generate_diff(file1, file2, format_name=stylish):
    dict1 = load_file_by_format(file1)
    dict2 = load_file_by_format(file2)
    #if format_name == stylish:
        #make_format = stylish()
    #if format_name == plain:
        #make_format = plain()
    #if format_name == json:
        #make_format = make_json_format()
    return stylish(calc_diff(dict1, dict2))
