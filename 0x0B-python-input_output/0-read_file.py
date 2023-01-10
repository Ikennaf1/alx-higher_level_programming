#!/usr/bin/python3

"""
A function module
"""


def read_file(filename=""):
    """
    Safely opens and reads a file
    """
    with open(filename, 'r', encoding="utf-8") as f:
        read_data = f.read()
    f.close()
    print(read_data, end="")
