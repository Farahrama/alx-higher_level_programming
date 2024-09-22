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
        with open("Square.json", "w") as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) <= 0:
            return []
        json_rep = json.loads(json_string)
        return json_rep

    @classmethod
    def create(cls, **dictionary):
        from models.rectangle import Rectangle
        from models.square import Square
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        if cls.__name__ == "Square":
            obj = cls(1)
        obj.update(**dictionary)
        return (obj)

    @classmethod
    def load_from_file(cls):
        """that returns a list of instances:"""
        try: 
            with open("Rectangle.json", "r") as file:
                json_string = file.read()
                dict = cls.from_json_string(json_string)
        except FileNotFoundError:
            return []
        list_of_instance = [cls.create(**i) for i in dict ]
        return list_of_instance
