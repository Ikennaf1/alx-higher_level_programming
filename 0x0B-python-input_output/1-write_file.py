#!/usr/bin/python3

"""
A python Module
"""


def write_file(filename="", text=""):
    """
    Open and write to a file

    Returns:
        `int`: Number of chars written
    """
    with open(filename, 'w', encoding="utf-8") as f:
        chars_written = f.write(text)
    f.close()
    return chars_written
