OPEN_BRACKET = '{'
CLOSE_BRACKET = '}'
TAB = '  '
LINE_BREAK = '\n'
UNCHANGED = '    '
ADDED = '  + '
REMOVED = '  - '


def render(diff_dict, depth=0):
    indent = TAB * depth
    result = OPEN_BRACKET + LINE_BREAK
    indent2 = indent * (depth - 1)
    for key, node in diff_dict.items():
        if node['STATUS'] == 'HASCHILD':
            result += f"{indent}{UNCHANGED}{key}: " \
                      f"{render(node['CHILDREN'], depth + 2)}" \
                      f"{LINE_BREAK}"
        elif node['STATUS'] in ['UNCHANGED', 'ADDED', 'REMOVED']:
            result += f"{indent}{format_key(key, node)}: " \
                      f"{to_str(node['VALUE'], indent2)}\n"
        elif node['STATUS'] == 'CHANGED':
            result += f"{indent}{REMOVED}{key}: " \
                      f"{to_str(node['VALUE1'], indent2)}\n"
            result += f"{indent}{ADDED}{key}: " \
                      f"{to_str(node['VALUE2'], indent2)}\n"
    close_bracket_indent = TAB * depth
    result += close_bracket_indent + CLOSE_BRACKET
    return result


def to_str(value, indent=''):
    if value is None:
        return 'null'
    if isinstance(value, bool):
        return str(value).lower()
    if not isinstance(value, dict):
        return str(value)

    def walk(node, depth=1):
        result = ''
        tab = 2 * TAB
        ind_1 = indent + tab * (depth + 2)
        for key, value in node.items():
            if isinstance(value, dict):
                result += ind_1 + key + ': {\n' + walk(value, depth + 1) + '\n'
            else:
                result += ind_1 + key + f': {value}' + '\n'
        close_bracket_indent = indent + tab * (depth + 1)
        result += close_bracket_indent + '}'
        return result
    return '{\n' + walk(value, 0)


def format_key(key, value):
    if value['STATUS'] == 'UNCHANGED':
        return UNCHANGED + key
    elif value['STATUS'] == 'REMOVED':
        return REMOVED + key
    elif value['STATUS'] == 'ADDED':
        return ADDED + key
