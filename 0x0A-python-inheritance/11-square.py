#!/usr/bin/python3
"""class Square that inherits from Rectangle (9-rectangle.py).
(task based on 10-square.py)."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ that inherits from Rectangle (9-rectangle.py)"""
    def __init__(self, size):
        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__width = size
        self.__height = size
        self.__size = size    

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)