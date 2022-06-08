# !/usr/bin/env python3
import itertools
from gendiff.value import make_to_string


def update_value(value):
    if isinstance(value, dict):
        return '[complex value]'
    return value


def format_value(value):
    new_value = make_to_string(update_value(value))
    exceptions = ['[complex value]', 'null', 'true', 'false']
    if new_value in exceptions:
        return new_value
    elif isinstance(new_value, int):
        return new_value
    else:
        return f"'{new_value}'"


def build_suffix(some_dict):
    if some_dict['STATUS'] == 'ADDED':
        return f"added with value: {format_value(some_dict['VALUE'])}"
    if some_dict['STATUS'] == 'REMOVED':
        return "removed"
    if some_dict['STATUS'] == 'CHANGED':
        return f"updated. From {format_value(some_dict['VALUE1'])} " \
               f"to {format_value(some_dict['VALUE2'])}"


def render(diff_dict):
    result_list = []
    for k, v in diff_dict.items():
        if v['STATUS'] in ['CHANGED', 'ADDED', 'REMOVED']:
            result_list.append(f'Property \'{k}\''
                               f' was {build_suffix(v)}')
        elif v['STATUS'] == 'UNCHANGED':
            result_list = result_list
        elif v['STATUS'] == 'HASCHILD':
            result_list.append(make_format_for_child(v, k))
    result = itertools.chain(result_list)
    return '\n'.join(result)


def make_format_for_child(value, key):
    parent = key
    child = value['CHILDREN']
    result_list = []
    for key_, val in child.items():
        if val['STATUS'] in ['CHANGED', 'ADDED', 'REMOVED']:
            result_list.append(f"Property '{parent}.{key_}'"
                               f" was {build_suffix(val)}")
        elif val['STATUS'] == 'UNCHANGED':
            result_list = result_list
        elif val['STATUS'] == 'HASCHILD':
            next_parent = f'{parent}.{key_}'
            result_list.append(make_format_for_child(val, next_parent))
    return '\n'.join(result_list)
