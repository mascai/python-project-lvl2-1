"""The parser module."""


import argparse

from gendiff import generate_diff


def run_parse():
    """Init of parser objects."""
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', default='plain',  # noqa: WPS317
                        choices=['plain', 'cascade', 'json'],   # noqa: WPS318
                        help='set format of output',
                        )
    args = parser.parse_args()
    print(generate_diff(args.first_file, args.second_file, args.format))
