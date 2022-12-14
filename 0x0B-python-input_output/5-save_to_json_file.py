#!/usr/bin/python3

"""
A python Module
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Saves object string to file as json
    """
    with open(filename, 'w', encoding="utf-8") as f:
        chars_written = f.write(json.dumps(my_obj))
    f.close()

    return chars_written
