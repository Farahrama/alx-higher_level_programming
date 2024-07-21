#!/usr/bin/python3
"""Square that defines a square by: (based on 2-square.py)"""


class Square:
    """Represents a square"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Returns the area of the square."""
        return self.__size ** 2
