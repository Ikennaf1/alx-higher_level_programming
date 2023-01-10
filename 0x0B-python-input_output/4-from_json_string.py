#!/usr/bin/python3

"""
A python module
"""


import json


def from_json_string(my_str):
    """
    Converts from json to object
    """
    return json.loads(my_str)
