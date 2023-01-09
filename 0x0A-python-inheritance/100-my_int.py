#!/usr/bin/python3

"""
A rebel int class
"""


class MyInt(int):
    """
    A rebel int class
    """

    def __new__(cls, my_int):
        """
        Negates the supplied int

        Args:
            my_int: `int` The given integer
        Returns:
            `int`: `int`
        """
        return super(MyInt, cls).__new__(cls, my_int * -1)
