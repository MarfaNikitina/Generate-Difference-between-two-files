# !/usr/bin/env python3
from gendiff.generate_diff import  convert_value


def update_value(value):
    if not isinstance(value, str):
        value = '[complex value]'
    else:
        value
    return value


def plain(dict1, dict2):
    status_dict = create_status_dict(dict1, dict2)
    result_list = []
    for k in status_dict:
        if status_dict[k] == 'added':
            result_list.append(
                f"Property '{k}' was added with value: {convert_value(update_value(dict2[k]))}"
            )
        elif status_dict[k] == 'deleted':
            result_list.append(f"Property '{k}' was removed")
        elif status_dict[k] == 'changed':
            result_list.append(
                f"Propetry '{k}' was updated. "
                f"From {convert_value(update_value(dict1[k]))} to {convert_value(update_value(dict2[k]))} "
            )
        elif status_dict[k] == 'unchanged':
            if isinstance(dict1[k], dict) and isinstance(dict2[k], dict):
                result_list.append(plain(dict1[k], dict2[k]))
            else:
                result_list = result_list
    return result_list