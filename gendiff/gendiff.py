from gendiff.formatter import format
from gendiff.parser import parse
from gendiff.diff_tree import calculate_diff
import os


def generate_diff(file1, file2, format_type='stylish'):
    first_data = get_data(file1)
    second_data = get_data(file2)
    diff = calculate_diff(first_data, second_data)
    return format(diff, format_type)


def get_data(some_file):
    with open(some_file, "r") as data:
        required_data = parse(data, os.path.splitext(some_file)[1][1:])
        return required_data
