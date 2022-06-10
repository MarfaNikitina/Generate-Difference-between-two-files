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
    for k, v in diff_dict.items():
        if v['STATUS'] == 'HASCHILD':
            result += f"{indent}{UNCHANGED}{k}: " \
                      f"{render(v['CHILDREN'], depth + 2)}" \
                      f"{LINE_BREAK}"
        elif v['STATUS'] in ['UNCHANGED', 'ADDED', 'REMOVED']:
            result += f"{indent}{format_key(k, v)}: " \
                      f"{format_value_to_string(v['VALUE'], indent2)}\n"
        elif v['STATUS'] == 'CHANGED':
            result += f"{indent}{REMOVED}{k}: " \
                      f"{format_value_to_string(v['VALUE1'], indent2)}\n"
            result += f"{indent}{ADDED}{k}: " \
                      f"{format_value_to_string(v['VALUE2'], indent2)}\n"
    close_bracket_indent = TAB * depth
    result += close_bracket_indent + CLOSE_BRACKET
    return result


def format_value_to_string(value, indent1=''):
    if value is True:
        value = 'true'
    elif value is False:
        value = 'false'
    elif value is None:
        value = 'null'
    if not isinstance(value, dict):
        return str(value)

    def walk(node, depth=1):
        result = ''
        tab = 2 * TAB
        current_ind = indent1 + tab * (depth + 2)
        for k, v in node.items():
            if isinstance(v, dict):
                result += current_ind + k + ': {\n' + walk(v, depth + 1) + '\n'
            else:
                result += current_ind + k + f': {v}' + '\n'
        close_bracket_indent = indent1 + tab * (depth + 1)
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
