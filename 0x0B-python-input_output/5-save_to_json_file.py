#!/usr/bin/python3
"""function that writes Object to a text file, using a JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, "w") as file:
        json.dump(my_obj, file)
