#!/usr/bin/python3

"""
A python Module
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Saves object string to file as json
    """
    my_json = json.dumps(my_obj)
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(my_json)
    f.close()
