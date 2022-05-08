# !/usr/bin/env python3
import json
import yaml


def convert_value(value):
    if value is True:
        value = 'true'
    elif value is False:
        value = 'false'
    elif value is None:
        value = 'null'
    return value

def load_file_by_format(file):
    if file.endswith(".json"):
        loaded_file = json.load(open(f'tests/fixtures/{file}'))
    elif file.endswith(".yml") or file.endswith(".yaml"):
        loaded_file = yaml.safe_load(open(f'tests/fixtures/{file}'))
    return loaded_file


def generate_diff(file1, file2):
    dict1 = load_file_by_format(file1)
    dict2 = load_file_by_format(file2)
    sorted_keys_set = sorted(set(dict1.keys()).union(set(dict2.keys())))
    result_diff = ''
    for key in sorted_keys_set:
        if key in dict1.keys() and key in dict2.keys():
            if dict1[key] == dict2[key]:
                result_diff += f'\n  {key}: {convert_value(dict1[key])}'
            else:
                result_diff += f'\n- {key}: {convert_value(dict1[key])}' \
                               f'\n+ {key}: {convert_value(dict2[key])}'
        elif key in dict1.keys() and key not in dict2.keys():
            result_diff += f'\n- {key}: {convert_value(dict1[key])}'
        elif key not in dict1.keys() and key in dict2.keys():
            result_diff += f'\n+ {key}: {convert_value(dict2[key])}'
    generated_diff = '{' + ''.join(result_diff) + '\n}'
    return generated_diff
