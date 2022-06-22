import itertools


def render(diff):
    return travel(diff)


def travel(diff, path=''):
    lines = []
    for key, value in diff.items():
        if value['STATUS'] in ['CHANGED', 'ADDED', 'REMOVED']:
            lines.append(f'Property \'{path}{key}\''
                         f' {build_suffix(value)}')
        elif value['STATUS'] == 'HASCHILD':
            child = value['CHILDREN']
            lines.append(travel(child, path + key + '.'))
    result = itertools.chain(lines)
    return '\n'.join(result)


def to_str(value):
    if isinstance(value, dict):
        return '[complex value]'
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if isinstance(value, str):
        return f"'{value}'"
    return value


def build_suffix(node):
    if node['STATUS'] == 'ADDED':
        return f"was added with value: {to_str(node['VALUE'])}"
    if node['STATUS'] == 'REMOVED':
        return "was removed"
    if node['STATUS'] == 'CHANGED':
        return f"was updated. From {to_str(node['VALUE1'])} " \
               f"to {to_str(node['VALUE2'])}"
