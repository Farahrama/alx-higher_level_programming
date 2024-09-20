#!/usr/bin/python3
"""base class"""
import json


class Base():
    """This class will be the “base” of all other classes in this project. """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """that returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) <= 0:
            return "[]"
        json_string = json.dumps(list_dictionaries)
        return json_string

    @classmethod
    def save_to_file(cls, list_objs):
        """that writes the JSON string representation of list_objs"""
        if list_objs is None or len(list_objs) <= 0:
            list_objs = []
        dicts = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(dicts)        
        with open("Rectangle.json", "w") as file:
            file.write(json_string)
