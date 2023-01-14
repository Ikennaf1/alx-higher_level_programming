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

    @property
    def size(self):
        """
        Returns the size of the square
        """
        return self.width

    @size.setter
    def size(self, val):
        """
        Sets the size
        """
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """
        Assigns attributes
        """
        argc = len(args)
        kwargc = len(kwargs)
        new_attrs = ['id', 'size', 'x', 'y']

        if argc > 4:
            argc = 4

        if argc > 0:
            for i in range(argc):
                setattr(self, new_attrs[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in new_attrs:
                    setattr(self, k, v)

    def to_dictionary(self):
        """
        Returns dictionary representation of a square
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }

    def __str__(self):
        """
        The string representation of square class
        """
        return "[Square] ({:d}) {:d}/{:d} - {:d}".format(self.id, self.x, self.y, self.width)
