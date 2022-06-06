from gendiff.formatters.stylish import render
from gendiff.formatters.json import structure
from gendiff.formatters.plain import unit_files


def make_format(diff, format_name):
    if format_name == 'stylish':
        return render(diff)
    if format_name == 'plain':
        return unit_files(diff)
    if format_name == 'json':
        return structure(diff)
