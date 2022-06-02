from gendiff.formatters.stylish import stylish
from gendiff.formatters.json import make_json_format
from gendiff.formatters.plain import make_plain_format


def make_format(format_name):
    if format_name == 'stylish':
        return stylish()
    if format_name == 'plain':
        return make_plain_format()
    if format_name == 'json':
        return make_json_format()
