# !/usr/bin/env python3
from gendiff import generate_diff
import pytest
import os


TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
FIXTURES_PATH = f"{TESTS_DIR}/fixtures"


@pytest.mark.parametrize(
    "file1,file2,{filepath}",
    [("file1.json", "file2.json",
      {'STYLISH': "file1file2_json_diff.txt",
       'PLAIN': "f1f2plain_diff.txt",
       'JSON': "f1f2json_diff.txt"}),
        ("file1.yml", "file2.yml",
         {'STYLISH': "file1file2_yml_diff.txt",
          'PLAIN': "f1f2plain_diff.txt",
          'JSON': "f1f2json_diff.txt"}),
     ("file1tree.json", "file2tree.json",
      {'STYLISH': "f12tree_diff.txt",
       'PLAIN': "plain_diff.txt",
       'JSON': "jsondiff.txt"}),
        ("file1tree.yml", "file2tree.yml",
         {'STYLISH': "f12tree_diff.txt",
          'PLAIN': "plain_diff.txt",
          'JSON': "jsondiff.txt"}
         )])
def test_gendiff(file1, file2, filepath):
    f1 = f"{FIXTURES_PATH}/{file1}"
    f2 = f"{FIXTURES_PATH}/{file2}"
    expected = open(f"{FIXTURES_PATH}/{filepath['STYLISH']}", "r").read()
    expected_plain = open(f"{FIXTURES_PATH}/{filepath['PLAIN']}", "r").read()
    expected_json = open(f"{FIXTURES_PATH}/{filepath['JSON']}", "r").read()
    assert generate_diff(f1, f2) == expected
    assert generate_diff(f1, f2, format_type='plain') == expected_plain
    assert generate_diff(f1, f2, format_type='json') == expected_json
