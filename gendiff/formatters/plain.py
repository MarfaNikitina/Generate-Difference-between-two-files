# !/usr/bin/env python3
import itertools
from gendiff.formatters.stylish import convert_value


def update_value(value):
    if isinstance(value, dict):
        value = '[complex value]'
    else:
        value
    return value


def get_name(k, v):
    name = ''
    if v['STATUS'] in ['ADDED', 'DELETED', 'CHANGED', 'UNCHANGED']:
        return name + k

    child = v['CHILDREN']
    parent = k
    list_ = []
    for k, v in child.items():
        list_.append(parent)
        list_.append(get_name(k, v))
        name += '.'.join(list_)
        return name


def format_value(value):
    new_value = convert_value(update_value(value))
    exceptions = ['[complex value]', 'null', 'true', 'false']
    if new_value in exceptions:
        return new_value
    else:
        return "'" + new_value + "'"


def make_plain_format(diff_dict):
    result_list = []
    # key = get_name({k: v})
    for k, v in diff_dict.items():
        key = get_name(k, v)
        print(key)
        if v['STATUS'] == 'HASCHILD':
            # name = get_name(k, v)
            result_list.append(make_plain_format(v['CHILDREN']))
        elif v['STATUS'] == 'ADDED':
            result_list.append(f"Property '{key}' was added with value: " + format_value(v['VALUE']))
        elif v['STATUS'] == 'DELETED':
            result_list.append(f"Property '{key}' was removed")
        elif v['STATUS'] == 'CHANGED':
            result_list.append(
                f"Property '{key}' was updated. From " + format_value(v['VALUE1']) +
                ' to ' + format_value(v['VALUE2'])
            )
        elif v['STATUS'] == 'UNCHANGED':
            result_list = result_list
        result = itertools.chain(result_list)
    return '\n'.join(result)