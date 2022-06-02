def make_format(format_name):
    if format_name == 'stylish':
        make_format = stylish()
    if format_name == 'plain':
        make_format = make_plain_format()
    if format_name == 'json':
        make_format = make_json_format()
    return make_format
