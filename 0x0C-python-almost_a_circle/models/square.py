#!/usr/bin/python3
""" class Square that inherits from Rectangle"""
from models.rectangle import Rectangle

class Square(Rectangle):
    """inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)        

    @property
    def size(self):
        return self.__width

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value <= 0:
            raise ValueError("size must be > 0")
        self.width = value
        self.height = value
