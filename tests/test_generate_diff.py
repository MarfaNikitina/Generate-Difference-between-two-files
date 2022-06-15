from gendiff import generate_diff
import pytest
import os


TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
FIXTURES_PATH = f"{TESTS_DIR}/fixtures"


@pytest.mark.parametrize(
    'file1, file2, expected_sample_path, format',
    [("file1.json", "file2.json", "file1file2_json_diff.txt", "stylish"),
     ("file1.yml", "file2.yml", "file1file2_json_diff.txt", "stylish"),
     ("file1.json", "file2.json", "f1f2plain_diff.txt", "plain"),
     ("file1.yml", "file2.yml", "f1f2plain_diff.txt", "plain"),
     ("file1.json", "file2.json", "f1f2json_diff.txt", "json"),
     ("file1.yml", "file2.yml", "f1f2json_diff.txt", "json"),
     ("file1tree.json", "file2tree.json", "f12tree_diff.txt", "stylish"),
     ("file1tree.yml", "file2tree.yml", "f12tree_diff.txt", "stylish"),
     ("file1tree.json", "file2tree.json", "plain_diff.txt", "plain"),
     ("file1tree.yml", "file2tree.yml", "plain_diff.txt", "plain"),
     ("file1tree.json", "file2tree.json", "jsondiff.txt", "json"),
     ("file1tree.yml", "file2tree.yml", "jsondiff.txt", "json")
     ])
def test_gendiff(file1, file2, expected_sample_path, format):
    f1 = f"{FIXTURES_PATH}/{file1}"
    f2 = f"{FIXTURES_PATH}/{file2}"
    with open(f"{FIXTURES_PATH}/{expected_sample_path}", "r") as data:
        expected = data.read()
    assert generate_diff(f1, f2, format) == expected
