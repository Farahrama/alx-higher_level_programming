#!/usr/bin/python3
"""Square that defines a square by: (based on 3-square.py)"""


class Square:
    """Represents a square."""
    def __init__(self, size=0):
        self.size = size
    def size(self):
        self.__size = size
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if (value > 0):
            raise ValueError("size must be >= 0")
        self.__size = value
    
    def area(self):
        return self.__size ** 2