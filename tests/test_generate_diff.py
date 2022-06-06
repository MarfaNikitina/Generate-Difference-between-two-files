# !/usr/bin/env python3
from gendiff import generate_diff
import pytest
import os


TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
FIXTURES_PATH = f"{TESTS_DIR}/fixtures"


@pytest.mark.parametrize(
    "test_input,expected",
    [((f"{FIXTURES_PATH}/file1.json",
      f"{FIXTURES_PATH}/file2.json"),
      open(f"{FIXTURES_PATH}/file1file2_json_diff.txt", "r").read()),
        ((f"{FIXTURES_PATH}/file1.yml",
            f"{FIXTURES_PATH}/file2.yml"),
            open(f"{FIXTURES_PATH}/f1f2_yml_diff.txt", "r").read()),
        ((f"{FIXTURES_PATH}/file1tree.json",
            f"{FIXTURES_PATH}/file2tree.json"),
            open(f"{FIXTURES_PATH}/f12tree_diff.txt", "r").read()),
        ((f"{FIXTURES_PATH}/file1tree.yml",
            f"{FIXTURES_PATH}/file2tree.yml"),
            open(f"{FIXTURES_PATH}/f12tree_diff.txt", "r").read())
     ])
def test_gendiff(test_input, expected):
    assert generate_diff(test_input[0], test_input[1]) == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [((f"{FIXTURES_PATH}/file1.json",
      f"{FIXTURES_PATH}/file2.json"),
      open(f"{FIXTURES_PATH}/f1f2plain_diff.txt", "r").read()),
        ((f"{FIXTURES_PATH}/file1.yml",
            f"{FIXTURES_PATH}/file2.yml"),
            open(f"{FIXTURES_PATH}/f1f2plain_diff.txt", "r").read()),
        ((f"{FIXTURES_PATH}/file1tree.json",
            f"{FIXTURES_PATH}/file2tree.json"),
            open(f"{FIXTURES_PATH}/plain_diff.txt", "r").read()),
        ((f"{FIXTURES_PATH}/file1tree.yml",
            f"{FIXTURES_PATH}/file2tree.yml"),
            open(f"{FIXTURES_PATH}/plain_diff.txt", "r").read())
     ])
def test_plain_gendiff(test_input, expected):
    assert generate_diff(test_input[0], test_input[1], format_name='plain') == expected


@pytest.mark.parametrize(
    "test_input,expected",
    [((f"{FIXTURES_PATH}/file1.json",
      f"{FIXTURES_PATH}/file2.json"),
      open(f"{FIXTURES_PATH}/f1f2json_diff.txt", "r").read()),
        ((f"{FIXTURES_PATH}/file1.yml",
            f"{FIXTURES_PATH}/file2.yml"),
            open(f"{FIXTURES_PATH}/f1f2json_diff.txt", "r").read()),
        ((f"{FIXTURES_PATH}/file1tree.json",
            f"{FIXTURES_PATH}/file2tree.json"),
            open(f"{FIXTURES_PATH}/jsondiff.txt", "r").read()),
     ((f"{FIXTURES_PATH}/file1tree.yml",
       f"{FIXTURES_PATH}/file2tree.yml"),
      open(f"{FIXTURES_PATH}/jsondiff.txt", "r").read())
     ])
def test_json_gendiff(test_input, expected):
    assert generate_diff(test_input[0], test_input[1], format_name='json') == expected
