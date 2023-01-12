#!/usr/bin/python3

"""
A Python Class
"""


class Base:
    """
    A python base class

    Attr:
        __nb_objects: `int`
        id: `int`
    """

    __nb_objects = 0
    id = 0

    def __init__(self, id=None):
        """
        The constructor

        Args:
            id: `int`
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
