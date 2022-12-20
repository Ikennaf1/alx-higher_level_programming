#!/usr/bin/python3

class Square:
    def __init__(self, size=0):
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self._size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
        else:
            x = self.__size
            while x > 0:
                y = self.__size
                while y > 0:
                    print("#", end="")
                    y -= 1
                print()
                x -= 1
