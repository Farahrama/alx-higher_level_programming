#!/usr/bin/python3
"""class BaseGeometry (based on 6-base_geometry.py)."""


class BaseGeometry:
    """this class based on 6-base_geometry.py"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = ""
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")