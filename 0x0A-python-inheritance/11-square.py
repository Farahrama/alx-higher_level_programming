#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
"""class Square that inherits from Rectangle (9-rectangle.py).
(task based on 10-square.py)."""

class Square(Rectangle):

    def __init__(self, size):
        super().__init__(size, size)
        super().integer_validator("size", size)
        self.__width = size
        self.__height = size
        self.__size = size    
