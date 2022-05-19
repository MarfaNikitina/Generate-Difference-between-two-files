# !/usr/bin/env python3


OPEN_BRACKET = '{'
CLOSE_BRACKET = '}'
TAB = '  '
LINE_BREAK = '\n'
EMPTY = '    '
PLUS = '  + '
MINUS = '  - '
COLON = ': '


def convert_value(value):
    if value is True:
        value = 'true'
    elif value is False:
        value = 'false'
    elif value is None:
        value = 'null'
    return value


def stylish(diff_dict, depth=0):
    indent = TAB * depth
    res = OPEN_BRACKET + LINE_BREAK
    for k, v in diff_dict.items():
        if v['STATUS'] == 'HASCHILD':
            res += f"{indent}{EMPTY}{k}: " \
                   f"{stylish(v['CHILDREN'], depth + 2)}{LINE_BREAK}"
        elif v['STATUS'] in ['UNCHANGED', 'ADDED', 'DELETED']:
            res += f"{indent}{format_k(k, v)}: "\
                   f"{format_value_to_str(v['VALUE'], indent * (depth - 1))}\n"
        elif v['STATUS'] == 'CHANGED':
            res += f"{indent}{MINUS}{k}: " \
                   f"{format_value_to_str(v['VALUE1'], indent * (depth - 1))}\n"
            res += f"{indent}{PLUS}{k}: " \
                   f"{format_value_to_str(v['VALUE2'], indent * (depth - 1))}\n"
    close_bracket_indent = TAB * depth
    res += close_bracket_indent + CLOSE_BRACKET
    return res


def format_value_to_str(some_value, indent1=''):
    value = convert_value(some_value)
    if not isinstance(value, dict):
        return str(value)

    def walk(node, depth=1):
        result = ''
        tab = '    '
        for k, v in node.items():
            if isinstance(v, dict):
                result += indent1 + tab * (depth + 2) + str(k) + COLON + '{' + '\n' + walk(v, depth + 1) + '\n'
            else:
                result += indent1 + tab * (depth + 2) + str(k) + f': {v}' + '\n'
        close_bracket_indent = indent1 + tab * (depth + 1)
        result += close_bracket_indent + '}'
        return result
    return '{\n' + walk(value, 0)


def format_k(k, v):
    if v['STATUS'] == 'UNCHANGED':
        return EMPTY + k
    elif v['STATUS'] == 'DELETED':
        return MINUS + k
    elif v['STATUS'] == 'ADDED':
        return PLUS + k