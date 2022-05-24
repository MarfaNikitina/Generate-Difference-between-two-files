# !/usr/bin/env python3
import itertools
from gendiff.formatters.stylish import convert_value


def update_value(value):
    if isinstance(value, dict):
        value = '[complex value]'
    else:
        value
    return value


def format_value(value):
    new_value = convert_value(update_value(value))
    exceptions = ['[complex value]', 'null', 'true', 'false']
    if new_value in exceptions:
        return new_value
    else:
        return "'" + new_value + "'"


def create_end_by_status(v):
    if v['STATUS'] == 'ADDED':
        return f"added with value: {format_value(v['VALUE'])}"
    elif v['STATUS'] == 'DELETED':
        return "removed"
    elif v['STATUS'] == 'CHANGED':
        return f"updated. From {format_value(v['VALUE1'])} " \
               f"to {format_value(v['VALUE2'])}"


def make_plain_format(diff_dict):
    result_list = []
    for k, v in diff_dict.items():
        if v['STATUS'] in ['CHANGED', 'ADDED', 'DELETED']:
            result_list.append(f'Property \'{k}\''
                               f' was {create_end_by_status(v)}')
        elif v['STATUS'] == 'UNCHANGED':
            result_list = result_list
        elif v['STATUS'] == 'HASCHILD':
            result_list.append(plain_for_child(v, k))
        result = itertools.chain(result_list)
    return '\n'.join(result)


def plain_for_child(v, k):
    parent = k
    child = v['CHILDREN']
    result_list = []
    for key, val in child.items():
        if val['STATUS'] in ['CHANGED', 'ADDED', 'DELETED']:
            result_list.append(f"Property '{parent}.{key}'"
                               f" was {create_end_by_status(val)}")
        elif val['STATUS'] == 'UNCHANGED':
            result_list = result_list
        elif val['STATUS'] == 'HASCHILD':
            new_parent = f'{parent}.{key}'
            result_list.append(plain_for_child(val, new_parent))
    return '\n'.join(result_list)
