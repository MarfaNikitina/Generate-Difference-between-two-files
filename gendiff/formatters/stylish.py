# !/usr/bin/env python3
#from gendiff.generate_diff import convert_value


OPEN_BRACKET = '{'
CLOSE_BRACKET = '}'
TAB = '  '
LINE_BREAK = '\n'
COLON = ': '
EMPTY = '  '
PLUS = '+ '
MINUS = '- '


def build_diff(dict1, dict2):
    status_dict = create_status_dict(dict1, dict2)
    res_dict = {}
    for k in status_dict:
        if status_dict[k] == 'unchanged':
            res_dict[k] = convert_value(dict1[k])
        elif status_dict[k] == 'changed':
            if isinstance(dict1[k], dict) and isinstance(dict2[k], dict):
                # res_dict['  ' + k] = build_diff(dict1[k], dict2[k])
                res_dict[k] = build_diff(dict1[k], dict2[k])
            else:
                res_dict['-' + k] = convert_value(dict1[k])
                res_dict['+' + k] = convert_value(dict2[k])
        elif status_dict[k] == 'deleted':
            res_dict['-' + k] = convert_value(dict1[k])
        elif status_dict[k] == 'added':
            res_dict['+' + k] = convert_value(dict2[k])
    # print(res_dict.keys(), res_dict.values())
    return res_dict


def stylish(dict1, dict2, depth=1):
    some_dict = build_diff(dict1, dict2)
    indent = TAB * depth
    res = OPEN_BRACKET + LINE_BREAK
    for k, v in some_dict.items():
        if k[0] in ('+', '-'):
            k = k[0] + ' ' + k[1:]
        else:
            k = '  ' + k
        if isinstance(v, dict):
            res += indent + k + COLON + stylish(v, depth + 2) + LINE_BREAK
        else:
            res += indent + k + COLON + str(v) + LINE_BREAK
    close_bracket_indent = TAB * (depth - 1)
    res += close_bracket_indent + CLOSE_BRACKET
    return res
