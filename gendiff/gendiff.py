from gendiff.formatter import format
from gendiff.parser import parse
from gendiff.structure import calculate_diff
import os


def generate_diff(file1, file2, format_type='stylish'):
    with open(file1, "r") as data:
        dict1 = parse(data, os.path.splitext(file1)[1])
    with open(file2, "r") as data:
        dict2 = parse(data, os.path.splitext(file2)[1])
    diff = calculate_diff(dict1, dict2)
    return format(diff, format_type)
