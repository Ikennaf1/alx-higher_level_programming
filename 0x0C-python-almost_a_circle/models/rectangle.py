#!/usr/bin/python3

"""
A python class
"""


from models.base import Base


class Rectangle(Base):
    """
    A Rectangle class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor for the Rectangle class
        """
        super().__init__(id)

        self.is_int(width, 'width')
        self.is_int(height, 'height')
        self.is_int(x, 'x')
        self.is_int(y, 'y')

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """
        Returns the width
        """
        return self.__width

    @width.setter
    def width(self, param):
        """
        Sets the width
        """
        self.is_int(param, 'width')
        self.__width = param

    @property
    def height(self):
        """
        Returns the height
        """
        return self.__height

    @height.setter
    def height(self, param):
        """
        Sets the height
        """
        self.is_int(param, 'height')
        self.__height = param

    @property
    def x(self):
        """
        Returns x
        """
        return self.__x

    @x.setter
    def x(self, param):
        """
        Sets x
        """
        self.is_int(param, 'x')
        self.__x = param

    @property
    def y(self):
        """
        Returns y
        """
        return self.__y

    @y.setter
    def y(self, param):
        """
        Sets y
        """
        self.is_int(param, 'y')
        self.__y = param

    def area(self):
        """
        Computes and returns the area of the rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Displays the rectangle with #
        """
        h = self.__height
        w = self.__width
        x = self.__x
        y = self.__y

        if self.area() <= 0:
            pass

        while y > 0:
            print()
            y -= 1

        while h > 0:
            w = self.__width
            x = self.__x
            while x > 0:
                print(" ", end="")
                x -= 1

            while w > 0:
                print("{}".format("#"), end="")
                w -= 1
            print()
            h -= 1

    def update(self, *args, **kwargs):
        """
        Assigns an argument to each attribute
        """
        argc = len(args)
        kwargc = len(kwargs)

        new_attrs = ['id', 'width', 'height', 'x', 'y']

        if argc > 5:
            argc = 5

        if argc > 0:
            for i in range(argc):
                setattr(self, new_attrs[i], args[i])
        elif kwargc > 0:
            for k, v in kwargs.items():
                if k in new_attrs:
                    setattr(self, k, v)

    def to_dictionary(self):
        """
        Returns dictionary representation of class
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def is_int(self, val, param):
        """
        Checks if supplied value is an integer
        """
        if type(val) is not int:
            raise TypeError(param + ' must be an integer')

        if val <= 0 and param in ('width', 'height'):
            raise ValueError(param + ' must be > 0')

        if val < 0 and param in ('x', 'y'):
            raise ValueError(param + ' must be >= 0')

    def __str__(self):
        """
        Returns string representation of class
        """
        return "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}".format(self.id, self.__x, self.__y, self.__width, self.__height)
