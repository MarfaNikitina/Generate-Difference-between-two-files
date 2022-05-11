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


def create_key_set(dict1, dict2):
    sorted_keys_set = sorted(set(dict1.keys()).union(set(dict2.keys())))
    return sorted_keys_set


def create_status_dict(dict1, dict2):
    sorted_keys_set = create_key_set(dict1, dict2)
    status_dict = {}
    for key in sorted_keys_set:
        if key in dict1 and key in dict2:
            if dict1[key] == dict2[key]:
                status_dict[key] = 'unchanged'
            else:
                status_dict[key] = 'changed'
        elif key in dict1 and key not in dict2:
            status_dict[key] = 'deleted'
        elif key not in dict1 and key in dict2:
            status_dict[key] = 'added'
    return status_dict


def build_diff(dict1, dict2):
    status_dict = create_status_dict(dict1, dict2)
    res_dict = {}
    for k in status_dict:
        if status_dict[k] == 'unchanged':
            res_dict[k] = convert_value(dict1[k])
        elif status_dict[k] == 'changed':
            if isinstance(dict1[k], dict) and isinstance(dict2[k], dict):
                # res_dict['  ' + k] = build_diff(dict1[k], dict2[k])
                res_dict[k] = build_diff(dict1[k], dict2[k])
            else:
                res_dict['-' + k] = convert_value(dict1[k])
                res_dict['+' + k] = convert_value(dict2[k])
        elif status_dict[k] == 'deleted':
            res_dict['-' + k] = convert_value(dict1[k])
        elif status_dict[k] == 'added':
            res_dict['+' + k] = convert_value(dict2[k])
    # print(res_dict.keys(), res_dict.values())
    return res_dict


def build_diff345(dict1, dict2):
    status_dict = create_status_dict(dict1, dict2)
    res_dict = {}
    for k in status_dict:
        if status_dict[k] == 'unchanged':
            res_dict[k] = convert_value(dict1[k])
        elif status_dict[k] == 'changed':
            if isinstance(dict1[k], dict) and isinstance(dict2[k], dict):
                # res_dict['  ' + k] = build_diff(dict1[k], dict2[k])
                res_dict[k] = build_diff(dict1[k], dict2[k])
            else:
                # res_dict['-' + k] = convert_value(dict1[k])
                # res_dict['+' + k] = convert_value(dict2[k])
                res_dict[k] = {
                    '-': convert_value(dict1[k]),
                    '+': convert_value(dict2[k]),
                }
        elif status_dict[k] == 'deleted':
            # res_dict['-' + k] = convert_value(dict1[k])
            res_dict[k] = {
                '-': convert_value(dict1[k])
            }
        elif status_dict[k] == 'added':
            # res_dict['+' + k] = convert_value(dict2[k])
            res_dict[k] = {
                '+': convert_value(dict2[k])
            }
    # print(res_dict.keys(), res_dict.values())
    return res_dict


OPEN_BRACKET = '{'
CLOSE_BRACKET = '}'
TAB = '  '
LINE_BREAK = '\n'
COLON = ':'


def stylish(some_dict, depth=1):  # indent=TAB
    # print(f'INDNET IS: "{indent}"')
    indent = TAB * depth
    res = OPEN_BRACKET + LINE_BREAK
    for k, v in some_dict.items():
        if k[0] in ('+', '-'):
            k = k[0] + ' ' + k[1:]
        else:
            k = '  ' + k
        if isinstance(v, dict):
            res += indent + k + ': ' + stylish(v, depth + 2) + '\n'
        else:
            print(k, f'"{v}"')
            res += indent + k + ': ' + str(v) + '\n'
    close_bracket_indent = TAB * (depth - 1)
    res += close_bracket_indent + '}'
    return res


def generate_diff(file1, file2):
    dict1 = load_file_by_format(file1)
    dict2 = load_file_by_format(file2)
    return stylish(build_diff(dict1, dict2))


def generate_diff1(file1, file2):
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
