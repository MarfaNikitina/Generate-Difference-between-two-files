# !/usr/bin/env python3


OPEN_BRACKET = '{'
CLOSE_BRACKET = '}'
TAB = '  '
LINE_BREAK = '\n'
COLON = ': '
EMPTY = '    '
PLUS = '  + '
MINUS = '  - '


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
            res += indent + EMPTY + k + COLON + stylish(v['CHILDREN'], depth + 2) + LINE_BREAK
        elif v['STATUS'] in ['UNCHANGED', 'ADDED', 'DELETED']:
            res += indent + format_k(k, v) + COLON + format_value_to_str(convert_value(v['VALUE'])) + LINE_BREAK
        elif v['STATUS'] == 'CHANGED':
            res += indent + MINUS + k + COLON + format_value_to_str(convert_value(v['VALUE1'])) + LINE_BREAK
            res += indent + PLUS + k + COLON + format_value_to_str(convert_value(v['VALUE2'])) + LINE_BREAK
    close_bracket_indent = TAB * depth
    res += close_bracket_indent + CLOSE_BRACKET
    return res


def format_value_to_str(value):
    if not isinstance(value, dict):
        return str(value)

    def walk(node, depth=1):
        result = ''
        tab = '    '
        for k, v in node.items():
            if isinstance(v, dict):
                result += tab * (depth + 2) + str(k) + ': {\n' + walk(v, depth + 1) + '\n'
            else:
                result += tab * (depth + 2) + str(k) + f': {v}' + '\n'
        close_bracket_indent = tab * (depth + 1)
        result += close_bracket_indent + '}'
        return result
    return '{\n' + walk(value, 0)


def format_k(k, v):
    if v['STATUS'] == 'UNCHANGED':
        key = EMPTY + k
    elif v['STATUS'] == 'DELETED':
        key = MINUS + k
    elif v['STATUS'] == 'ADDED':
        key = PLUS + k
    return key
