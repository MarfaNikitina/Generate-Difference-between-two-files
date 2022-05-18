# !/usr/bin/env python3
from gendiff.formatters.stylish import convert_value



def update_value(value):
    if isinstance(value, dict):
        value = '[complex value]'
    else:
        value
    return value


def get_name(node):
    #if not isinstance(node, dict):
        return node

        for k, v in node.items():
            if isinstance(v, dict):
                name.append(get_name(v))
            else:
                name.append(k)
    else:
        name.append(node)
    res = '.'. join(name)
    return res


def format_value(value):
    exceptions = ['[complex value]', 'null', 'true', 'false']
    if value in exceptions:
        return value
    else:
        return "'" + str(value) + "'"


def make_plain_format(diff_dict):
    result_list = []
    for k, v in diff_dict:
        key = get_name(k)
        if v['STATUS'] == 'HASCHILD':
            result_list.append(make_plain_format(v['CHILDREN'])
        elif v['STATUS'] == 'ADDED':
            result_list.append(
                f"Property '{k}' was added with value: " + format_value(convert_value(update_value(v['VALUE'])))
            )
        elif v['STATUS'] == 'DELETED':
            result_list.append(f"Property '{k}' was removed")
        elif v['STATUS'] == 'CHANGED':
                result_list.append(
                    f"Propetry '{k}' was updated. From " + format_value(convert_value(update_value(dict1[k]))) +
                    ' to ' + format_value(convert_value(update_value(dict2[k])))
                )
        elif status_dict[k] == 'unchanged':
            if isinstance(dict1[k], dict) and isinstance(dict2[k], dict):
                result_list.append(plain(dict1[k], dict2[k]))
            else:
                result_list = result_list
        result = itertools.chain(result_list)
    return '\n'.join(result)