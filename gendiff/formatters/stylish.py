TAB = '  '
UNCHANGED = '    '
ADDED = '  + '
REMOVED = '  - '


def render(diff_dict):
    return travel(diff_dict)


prefix_dict = {'UNCHANGED': UNCHANGED, 'ADDED': ADDED, 'REMOVED': REMOVED}


def travel(diff_dict, depth=0):
    indent = TAB * depth
    result = '{\n'
    new_indent = indent * (depth - 1)
    for key, node in diff_dict.items():
        if node['STATUS'] == 'HASCHILD':
            result += f"{indent}{UNCHANGED}{key}: " \
                      f"{travel(node['CHILDREN'], depth + 2)}\n"
        elif node['STATUS'] == 'CHANGED':
            result += f"{indent}{REMOVED}{key}: " \
                      f"{to_str(node['VALUE1'], new_indent)}\n"
            result += f"{indent}{ADDED}{key}: " \
                      f"{to_str(node['VALUE2'], new_indent)}\n"
        else:
            result += f"{indent}{prefix_dict[node['STATUS']]}{key}: " \
                      f"{to_str(node['VALUE'], new_indent)}\n"
    close_bracket_indent = TAB * depth
    result += close_bracket_indent + "}"
    return result


def to_str2(value, indent='', depth=1):
    if not isinstance(value, dict):
        if value is None:
            return 'null'
        if isinstance(value, bool) or isinstance(value, int):
            return str(value).lower()
        else:
            return str(value)
    result = '{\n'
    tab = 2 * TAB
    new_indent = indent + tab * (depth + 1)
    for key, val in value.items():
        result += f'{new_indent}{key}: ' \
                  f'{to_str2(val, indent, depth + 1)}\n'
    close_bracket_indent = indent + tab * depth
    result += close_bracket_indent + '}'
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
    else:
        return str(value)
