#!/usr/bin/python3
"""class Rectangle that inherits from Base"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle that inherits from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int and value <= 0:
            raise ValueError("width must be a positive integer")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int and value <= 0:
            raise ValueError("height must be a positive integer")
        self.__height = value

    @property
    def x(self, value):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int and value <= 0:
            raise ValueError("x must be a non-negative integer")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int and value <= 0:
            raise ValueError("y must be a non-negative integer")
        self.__y = value
