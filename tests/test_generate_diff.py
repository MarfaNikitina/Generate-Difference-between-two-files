# !/usr/bin/env python3
from gendiff import generate_diff
import pytest


@pytest.fixture
def f1_j():
    return 'file1.json'


@pytest.fixture
def f2_j():
    return 'file2.json'


@pytest.fixture
def resf1f2_j():
    return open(f'tests/fixtures/file1file2_json_diff.txt', "r").read()


@pytest.fixture
def f1_y():
    return 'file1.yml'


@pytest.fixture
def f2_y():
    return 'file2.yml'


@pytest.fixture
def resf1f2_y():
    return open(f'tests/fixtures/f1f2_yml_diff.txt', "r").read()


def test_generate_diff(f1_j, f2_j, resf1f2_j,
                       f1_y, f2_y, resf1f2_y):
    assert generate_diff(f1_j, f2_j) == resf1f2_j
    assert generate_diff(f1_y, f2_y) == resf1f2_y
