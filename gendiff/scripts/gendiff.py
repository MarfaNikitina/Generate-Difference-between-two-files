# !/usr/bin/env python3
from gendiff import generate_diff
from gendiff.parser_gendiff import make_parser


def main():
    args = make_parser()
    diff = generate_diff(args.first_file, args.second_file)
    print(diff)


if __name__ == '__main__':
    main()