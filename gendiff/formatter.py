from gendiff.formatters.stylish import make_stylish_format
from gendiff.formatters.json import make_json_format
from gendiff.formatters.plain import make_plain_format


def make_format(diff, format_name):
    if format_name == 'stylish':
        return make_stylish_format(diff)
    if format_name == 'plain':
        return make_plain_format(diff)
    if format_name == 'json':
        return make_json_format(diff)
