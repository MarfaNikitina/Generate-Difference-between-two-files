from gendiff.make_format import make_format
from parser_gendiff import load_file_by_format


def calculate_diff(dict1, dict2):
    res_dict = {}
    keys = sorted(set(dict1.keys()).union(set(dict2.keys())))
    for key in keys:
        res_dict[key] = make_status_value_for_key(dict1, dict2, key)
    return res_dict


def make_status_value_for_key(dict1, dict2, key):
    if isinstance(dict1.get(key), dict) and isinstance(dict2.get(key), dict):
        return {
            'STATUS': 'HASCHILD',
            'CHILDREN': calculate_diff(dict1[key], dict2[key])
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


def generate_diff(file1, file2, format_name='stylish'):
    dict1 = load_file_by_format(file1)
    dict2 = load_file_by_format(file2)
    diff = calculate_diff(dict1, dict2)
    return make_format(diff, format_name)
