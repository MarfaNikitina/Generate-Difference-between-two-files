from gendiff.format_value import make_value_to_string


OPEN_BRACKET = '{'
CLOSE_BRACKET = '}'
TAB = '  '
LINE_BREAK = '\n'
EMPTY = '    '
PLUS = '  + '
MINUS = '  - '


def make_stylish_format(diff_dict, depth=0):
    indent = TAB * depth
    result = OPEN_BRACKET + LINE_BREAK
    for k, v in diff_dict.items():
        if v['STATUS'] == 'HASCHILD':
            result += f"{indent}{EMPTY}{k}: " \
                      f"{make_stylish_format(v['CHILDREN'], depth + 2)}" \
                      f"{LINE_BREAK}"
        elif v['STATUS'] in ['UNCHANGED', 'ADDED', 'REMOVED']:
            result += f"{indent}{format_key(k, v)}: " \
                      f"{format_value_to_string(v['VALUE'], indent * (depth - 1))}" \
                      f"\n"
        elif v['STATUS'] == 'CHANGED':
            result += f"{indent}{MINUS}{k}: " \
                      f"{format_value_to_string(v['VALUE1'], indent * (depth - 1))}" \
                      f"\n"
            result += f"{indent}{PLUS}{k}: " \
                      f"{format_value_to_string(v['VALUE2'], indent * (depth - 1))}" \
                      f"\n"
    close_bracket_indent = TAB * depth
    result += close_bracket_indent + CLOSE_BRACKET
    return result


def format_value_to_string(some_value, indent1=''):
    value = make_value_to_string(some_value)
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
        return EMPTY + key
    elif value['STATUS'] == 'REMOVED':
        return MINUS + key
    elif value['STATUS'] == 'ADDED':
        return PLUS + key
