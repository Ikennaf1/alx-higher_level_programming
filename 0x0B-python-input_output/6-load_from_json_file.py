#!/usr/bin/python3

"""
A python module
"""


def load_from_json_file(filename):
    """
    creates object from json file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        my_obj = json.loads(f.read())
    f.close()
    return my_obj
