# !/usr/bin/env python3
import itertools
import json
import yaml
from gendiff.formatters.stylish import stylish
from gendiff.formatters.json import make_json_format
from gendiff.formatters.stylish import convert_value
#from gendiff.formatters.plain import make_plain_format


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


def update_value(value):
    if isinstance(value, dict):
        value = '[complex value]'
    else:
        value
    return value


def get_name(diff_dict):
    for k, v in diff_dict.items():
        name = []
        if v['STATUS'] == 'HASCHILD':
            name.append(get_name(v['CHILDREN']))
        else:
            name.append(k)
    result = '.'.join(name)
    return result

        #else:
            #return k
            #elif v['STATUS'] == ['CHANGED']:
        #if not isinstance(v['VALUE'], dict):
            #return k
        #else:
            #return k + '.' + get_name(v['VALUE'])


def format_value(value):
    new_value = convert_value(update_value(value))
    exceptions = ['[complex value]', 'null', 'true', 'false']
    if new_value in exceptions:
        return new_value
    else:
        return "'" + new_value + "'"


def make_plain_format(diff_dict):
    result_list = []
    for k, v in diff_dict.items():
        #key = get_name(k)
        if v['STATUS'] == 'HASCHILD':
            result_list.append(make_plain_format(v['CHILDREN']))
        elif v['STATUS'] == 'ADDED':
            result_list.append(f"Property '{get_name(diff_dict)}' was added with value: " + format_value(v['VALUE']))
        elif v['STATUS'] == 'DELETED':
            result_list.append(f"Property '{get_name(diff_dict)}' was removed")
        elif v['STATUS'] == 'CHANGED':
            result_list.append(
                f"Property '{get_name(diff_dict)}' was updated. From " + format_value(v['VALUE1']) +
                ' to ' + format_value(v['VALUE2'])
            )
        elif v['STATUS'] == 'UNCHANGED':
            result_list = result_list
        result = itertools.chain(result_list)
    return '\n'.join(result)


def generate_diff(file1, file2, format_name=stylish):
    dict1 = load_file_by_format(file1)
    dict2 = load_file_by_format(file2)
    #if format_name == stylish:
        #make_format = stylish()
    #if format_name == plain:
       # make_format = make_plain_format()
    #if format_name == json:
        #make_format = make_json_format()
    return make_plain_format(calc_diff(dict1, dict2))
