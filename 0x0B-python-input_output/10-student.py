#!/usr/bin/python3
"""class Student that defines a student by: (based on 9-student.py)"""


class Student:
    """defines a Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """based on 9-student.py"""
        if attrs is None:
            return self.__dict__
        else:
            return {attr: getattr(self, attr) \
                for attr in attrs if hasattr(self, attr)}
