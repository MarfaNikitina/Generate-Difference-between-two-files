from gendiff.formatters.stylish import render as render_stylish
from gendiff.formatters.json import render as render_json
from gendiff.formatters.plain import render as render_plain


def format(diff, format_type):
    if format_type == 'stylish':
        return render_stylish(diff)
    if format_type == 'plain':
        return render_plain(diff)
    if format_type == 'json':
        return render_json(diff)
