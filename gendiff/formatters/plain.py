# !/usr/bin/env python3
import itertools


def to_string(value):
    if isinstance(value, dict):
        return '[complex value]'
    if value is True:
        value = 'true'
    elif value is False:
        value = 'false'
    elif value is None:
        value = 'null'
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


def render(diff_dict, path=''):
    result_list = []
    for k, v in diff_dict.items():
        if v['STATUS'] in ['CHANGED', 'ADDED', 'REMOVED']:
            result_list.append(f'Property \'{path}{k}\''
                               f' {build_suffix(v)}')
        elif v['STATUS'] == 'HASCHILD':
            parent = k
            child = v['CHILDREN']
            new_path = path + parent + '.'
            result_list.append(render(child, new_path))
    result = itertools.chain(result_list)
    return '\n'.join(result)
