# !/usr/bin/env python3

def update_value(value):
    if not isinstance(value, str):
        value = '[complex value]'
    else:
        value
    return value


def get_name(node, prefix=''):
    complex_name = f'{prefix}.{node}'
    if not isinstance(node, dict):
        return node
    else:
        for k in node.keys():
            complex_name += get_name(k, complex_name)


def plain(dict1, dict2):
    status_dict = create_status_dict(dict1, dict2)
    result_list = []
    for k in status_dict:
        if status_dict[k] == 'added':
            result_list.append(
                f"Property '{get_name(k)}' was added with value: {convert_value(update_value(dict2[k]))}"
            )
        elif status_dict[k] == 'deleted':
            result_list.append(f"Property '{k}' was removed")
        elif status_dict[k] == 'changed':
            result_list.append(
                f"Propetry '{get_name(k)}' was updated. "
                f"From {convert_value(update_value(dict1[k]))} to {convert_value(update_value(dict2[k]))} "
            )
        elif status_dict[k] == 'unchanged':
            if isinstance(dict1[k], dict) and isinstance(dict2[k], dict):
                result_list.append(plain(dict1[k], dict2[k]))
            else:
                result_list = result_list
        result = itertools.chain(result_list)
    return '\n'.join(result)

def update_value(value):
    if isinstance(value, dict):
        value = '[complex value]'
    else:
        value
    return value


def get_name(node):
    name = []
    if isinstance(node, dict):
        for k, v in node.items():
            if isinstance(k, dict):
                name.append(get_name(node[k]))
            else:
                name.append(k)
    else:
        name.append(node)
    res = '.'. join(name)
    return res


def format_value(value):
    exceptions = [ '[complex value]', 'null', 'true', 'false']
    if value in exceptions:
        return value
    else:
        return "'" + str(value) + "'"


def plain(dict1, dict2):
    status_dict = create_status_dict(dict1, dict2)
    result_list = []
    for k in status_dict:
        key = get_name(k)
        if status_dict[k] == 'added':
            result_list.append(
                f"Property '{key}' was added with value: " + format_value(convert_value(update_value(dict2[k])))
            )
        elif status_dict[k] == 'deleted':
            result_list.append(f"Property '{key}' was removed")
        elif status_dict[k] == 'changed':
            if isinstance(dict1[k], dict) and isinstance(dict2[k], dict):
                result_list.append(plain(dict1[k], dict2[k]))
            else:
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