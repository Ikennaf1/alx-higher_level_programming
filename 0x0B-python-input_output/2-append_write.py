#!/usr/bin/python3

"""
A python module
"""


def append_write(filename="", text=""):
    """
    Append text to a file"
    """
    with open(filename, 'a', encoding="utf-8") as f:
        chars_written = f.write(text)
    f.close()
    return chars_written
