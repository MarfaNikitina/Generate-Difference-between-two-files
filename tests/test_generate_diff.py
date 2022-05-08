# !/usr/bin/env python3
from gendiff.generate_diff import generate_diff
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


def test_generate_diff(f1_j, f2_j, resf1f2_j):
    assert generate_diff(f1_j, f2_j) == resf1f2_j
