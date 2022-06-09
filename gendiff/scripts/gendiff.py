# !/usr/bin/env python3
from gendiff import generate_diff
from gendiff.cli import parse


FIXTURES_FILES_PATH = 'tests/fixtures'


def main():
    args = parse()
    diff = generate_diff(f'{FIXTURES_FILES_PATH}/{args.first_file}',
                         f'{FIXTURES_FILES_PATH}/{args.second_file}',
                         args.format)
    print(diff)


if __name__ == '__main__':
    main()
