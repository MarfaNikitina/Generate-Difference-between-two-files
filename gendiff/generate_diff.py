# !/usr/bin/env python3
import itertools
import json
import yaml
#from gendiff.formatters.stylish import stylish
#from gendiff.formatters.plain import plain


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


OPEN_BRACKET = '{'
CLOSE_BRACKET = '}'
TAB = '  '
LINE_BREAK = '\n'
COLON = ': '
EMPTY = '    '
PLUS = '  + '
MINUS = '  - '


def stylish(diff_dict, depth=0):
    # some_dict = calc_diff(dict1, dict2)
    print(diff_dict)
    indent = TAB * depth
    res = OPEN_BRACKET + LINE_BREAK
    for k, v in diff_dict.items():
        if v['STATUS'] == 'HASCHILD':
            res += indent + EMPTY + k + COLON + stylish(v['CHILDREN'], depth + 2) + LINE_BREAK
        #else:
            #if isinstance(v['VALUE'], dict):
                #res += indent + k + COLON + make_dict_to_string(v['VALUE']) + LINE_BREAK
        elif isinstance(v['VALUE'], dict):
            res += indent + format_k(diff_dict, k) + COLON + make_dict_to_string(v['VALUE']) + LINE_BREAK
        elif v['STATUS'] == 'CHANGED':
            res += indent + MINUS + k + COLON + str(v['VALUE1']) + LINE_BREAK
            res += indent + PLUS + k + COLON + str(v['VALUE2']) + LINE_BREAK
        else:
            res += indent + format_k(diff_dict, k) + COLON + str(v['VALUE']) + LINE_BREAK
    close_bracket_indent = TAB * (depth - 1)
    res += close_bracket_indent + CLOSE_BRACKET
    return res


def make_dict_to_string(some_dict, depth=1):
    result = ''
    TAB = '    '
    for k, v in some_dict.items():
        if isinstance(v, dict):
            result += TAB * (depth + 1) + str(k) + ': {\n' + make_dict_to_string(v, depth + 1) + '\n'
        else:
            result += TAB * (depth + 1) + str(k) + f': {v}' + '\n'
    close_bracket_indent = TAB * depth
    result += close_bracket_indent + '}'
    return '{\n' + result


def format_k(some_dict, key):
    for k, v in some_dict.items():
        if v['STATUS'] == 'UNCHANGED':
            key = EMPTY + k
        elif v['STATUS'] == 'DELETED':
            key = MINUS + k
        elif v['STATUS'] == 'ADDED':
            key = PLUS + k
    return key


def generate_diff(file1, file2, format_name=stylish):
    dict1 = load_file_by_format(file1)
    dict2 = load_file_by_format(file2)
    if format_name == stylish:
        make_format = stylish()
    #if format_name == plain:
        #make_format = plain()
    #if format_name == json:
        #make_format = make_json_format()
    return stylish(calc_diff(dict1, dict2))
