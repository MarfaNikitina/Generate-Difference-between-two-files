TAB = '  '
UNCHANGED = '    '
ADDED = '  + '
REMOVED = '  - '


def render(diff):
    return travel(diff)


def travel(diff, depth=0):
    prefix = {'UNCHANGED': UNCHANGED, 'ADDED': ADDED, 'REMOVED': REMOVED}
    indent = TAB * depth
    result = '{\n'
    new_indent = indent * (depth - 1)
    for key, node in diff.items():
        if node['STATUS'] == 'HASCHILD':
            result += f"{indent}{UNCHANGED}{key}: " \
                      f"{travel(node['CHILDREN'], depth + 2)}\n"
        elif node['STATUS'] == 'CHANGED':
            result += f"{indent}{REMOVED}{key}: " \
                      f"{to_str(node['VALUE1'], new_indent)}\n"
            result += f"{indent}{ADDED}{key}: " \
                      f"{to_str(node['VALUE2'], new_indent)}\n"
        else:
            result += f"{indent}{prefix[node['STATUS']]}{key}: " \
                      f"{to_str(node['VALUE'], new_indent)}\n"
    result += indent + "}"
    return result


def to_str(value, indent='', depth=1):
    if isinstance(value, bool):
        return str(value).lower()
    if value is None:
        return 'null'
    if isinstance(value, dict):
        result = '{\n'
        tab = 2 * TAB
        new_indent = indent + tab * (depth + 1)
        for key, val in value.items():
            result += f'{new_indent}{key}: ' \
                      f'{to_str(val, indent, depth + 1)}\n'
        close_bracket_indent = indent + tab * depth
        result += close_bracket_indent + '}'
        return result
    return str(value)
