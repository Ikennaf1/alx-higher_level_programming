#!/usr/bin/python3

"""
A Class Module
"""


class MyList(list):
    """
    Inherits from list
    """
    def print_sorted(self):
        """
        Prints list in sorted ascending order
        """
        if issubclass(MyList, list):
            print(sorted(self))
