# !/usr/bin/env python3
from gendiff import generate_diff
import file1file2_json.txt


def test_generate_diff():
    true_result = open(f'file1file2_json.txt', "r")
    assert generate_diff(file1.json, file2.json) == true_result
    assert generate_diff() == ''
