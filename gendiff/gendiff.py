from gendiff.formatter import format
from gendiff.parser import parse
from gendiff.diff_tree import calculate_diff
import os


def generate_diff(file1, file2, format_type='stylish'):
    dict1 = make_dict(file1)
    dict2 = make_dict(file2)
    diff = calculate_diff(dict1, dict2)
    return format(diff, format_type)


def make_dict(some_file):
    with open(some_file, "r") as data:
        dict_ = parse(data, os.path.splitext(some_file)[1][1:])
    return dict_
