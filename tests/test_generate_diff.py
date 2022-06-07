# !/usr/bin/env python3
from gendiff import generate_diff
import pytest
import os


TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
FIXTURES_PATH = f"{TESTS_DIR}/fixtures"


@pytest.mark.parametrize(
    "file1,file2,filepath",
    [("file1.json", "file2.json", "file1file2_json_diff.txt"),
        ("file1.yml", "file2.yml", "f1f2_yml_diff.txt"),
     ("file1tree.json", "file2tree.json", "f12tree_diff.txt"),
        ("file1tree.yml", "file2tree.yml", "f12tree_diff.txt")
     ])
def test_gendiff(file1, file2, filepath):
    f1 = f"{FIXTURES_PATH}/{file1}"
    f2 = f"{FIXTURES_PATH}/{file2}"
    expected = open(f"{FIXTURES_PATH}/{filepath}", "r").read()
    assert generate_diff(f1, f2) == expected


@pytest.mark.parametrize(
        "file1,file2,filepath",
        [("file1.json", "file2.json", "f1f2plain_diff.txt"),
            ("file1.yml", "file2.yml", "f1f2plain_diff.txt"),
            ("file1tree.json", "file2tree.json", "plain_diff.txt"),
            ("file1tree.yml", "file2tree.yml", "plain_diff.txt")
         ])
def test_plain_gendiff(file1, file2, filepath):
    f1 = f"{FIXTURES_PATH}/{file1}"
    f2 = f"{FIXTURES_PATH}/{file2}"
    expected = open(f"{FIXTURES_PATH}/{filepath}", "r").read()
    assert generate_diff(f1, f2, format_type='plain') == expected


@pytest.mark.parametrize(
        "file1,file2,filepath",
        [("file1.json", "file2.json", "f1f2json_diff.txt"),
            ("file1.yml", "file2.yml", "f1f2json_diff.txt"),
            ("file1tree.json", "file2tree.json", "jsondiff.txt"),
            ("file1tree.yml", "file2tree.yml", "jsondiff.txt")
         ])
def test_plain_gendiff(file1, file2, filepath):
    f1 = f"{FIXTURES_PATH}/{file1}"
    f2 = f"{FIXTURES_PATH}/{file2}"
    expected = open(f"{FIXTURES_PATH}/{filepath}", "r").read()
    assert generate_diff(f1, f2, format_type='json') == expected
