#!/usr/bin/python3

"""
A python class
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A square class derived from rectangle
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        The square constructor
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        The string representation of square class
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x, self.y, self.width)
