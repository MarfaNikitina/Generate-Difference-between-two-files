from gendiff.formatters.stylish import render
from gendiff.formatters.json import structure
from gendiff.formatters.plain import unit_files


def format(diff, format_type):
    if format_type == 'stylish':
        return render(diff)
    if format_type == 'plain':
        return unit_files(diff)
    if format_type == 'json':
        return structure(diff)
