#!/usr/bin/python3
"""class Student that defines a student"""


class Student:
    """defines a Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ that retrieves a dictionary representation of a Student"""
        return self.__dict__
