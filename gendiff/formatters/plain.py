# !/usr/bin/env python3
import itertools


def to_string(value):
    if value is True:
        value = 'true'
    elif value is False:
        value = 'false'
    elif value is None:
        value = 'null'
    if isinstance(value, dict):
        return '[complex value]'
    return value


def format_value(value):
    new_value = to_string(value)
    exceptions = ['[complex value]', 'null', 'true', 'false']
    if new_value in exceptions:
        return new_value
    elif isinstance(new_value, int):
        return new_value
    else:
        return f"'{new_value}'"


def build_suffix(node):
    if node['STATUS'] == 'ADDED':
        return f"was added with value: {format_value(node['VALUE'])}"
    if node['STATUS'] == 'REMOVED':
        return "was removed"
    if node['STATUS'] == 'CHANGED':
        return f"was updated. From {format_value(node['VALUE1'])} " \
               f"to {format_value(node['VALUE2'])}"


def render(diff_dict):
    result_list = []
    for k, v in diff_dict.items():
        if v['STATUS'] in ['CHANGED', 'ADDED', 'REMOVED']:
            result_list.append(f'Property \'{k}\''
                               f' {build_suffix(v)}')
        # elif v['STATUS'] == 'UNCHANGED':
            # result_list = result_list
        elif v['STATUS'] == 'HASCHILD':
            result_list.append(make_format_for_child(v, k))
        # else:
            # result_list
    result = itertools.chain(result_list)
    return '\n'.join(result)


def make_format_for_child(value, key):
    parent = key
    child = value['CHILDREN']
    result_list = []
    for key_, val in child.items():
        if val['STATUS'] in ['CHANGED', 'ADDED', 'REMOVED']:
            result_list.append(f"Property '{parent}.{key_}'"
                               f" {build_suffix(val)}")
        # elif val['STATUS'] == 'UNCHANGED':
            # result_list = result_list
        elif val['STATUS'] == 'HASCHILD':
            next_parent = f'{parent}.{key_}'
            result_list.append(make_format_for_child(val, next_parent))
    return '\n'.join(result_list)
