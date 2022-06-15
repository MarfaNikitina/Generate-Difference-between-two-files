import itertools


def to_str(value):
    if isinstance(value, dict):
        return '[complex value]'
    if value is None:
        return 'null'
    if isinstance(value, bool) or isinstance(value, int):
        return str(value).lower()
    if isinstance(value, str):
        return f"'{value}'"


def build_suffix(node):
    if node['STATUS'] == 'ADDED':
        return f"was added with value: {to_str(node['VALUE'])}"
    if node['STATUS'] == 'REMOVED':
        return "was removed"
    if node['STATUS'] == 'CHANGED':
        return f"was updated. From {to_str(node['VALUE1'])} " \
               f"to {to_str(node['VALUE2'])}"


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
