#!/usr/bin/env python

import json
import sys
from argparse import ArgumentParser

TESTS = (
    ({}, {}),
    ({'a': 1}, {'a': 1}),
    (
        {
            "a": 1,
            "b": True,
            "c": {
                "d": 3,
                "e": "test"
            }
        },
        {
            "a": 1,
            "b": True,
            "c.d": 3,
            "c.e": "test"
        }
    ),
)


# generator depth first recursive iteration
# over all keys and value dictionaries
def flatten(d, path=[]):
    for k, v in d.items():
        if isinstance(v, dict):
            for t in flatten(v, path + [k]):
                yield t
        else:
            yield path + [k], v


# use the DFS generator to create a dictionary
def flatten_to_dict(d):
    return {'.'.join(map(str, k)): v for k, v in flatten(d)}


def run_tests():
    for test, expected in TESTS:
        flat = flatten_to_dict(test)
        if flat == expected:
            sys.stdout.write(".")
        else:
            sys.stdout.write("E")
    sys.stdout.write("\n")


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument("--test", action="store_true", dest="test", default=False, help="run tests")
    parser.add_argument("filename", nargs='?', default=None, help="input filename, default: stdin")

    args = parser.parse_args()

    if args.test:
        run_tests()
    else:
        if args.filename:
            with open(args.filename, "r") as f:
                dictionary = json.load(fp=f)
        else:
            dictionary = json.load(fp=sys.stdin)

        json.dump(
            flatten_to_dict(dictionary),
            fp=sys.stdout,
            indent=True,
        )

        sys.stdout.write('\n')
