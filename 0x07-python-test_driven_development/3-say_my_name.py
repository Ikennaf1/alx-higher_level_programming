#!/usr/bin/python3
"""

Module that says my name 

"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name

    Args:
        first_name: `string`
        last_name: `string` optional

    Returns:
        Full name: `string`
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
