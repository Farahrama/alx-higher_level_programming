#!/usr/bin/python3
"""class Square that defines a square by: (based on 4-square.py)"""


class Square:
    """Represents a square."""
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.size ** 2

    def my_print(self):
        if self.size == 0:
            print()
        for i in range(self.size):
            print("#" * self.size)
