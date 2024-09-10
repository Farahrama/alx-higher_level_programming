#!/usr/bin/python3
"""function that returns the JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object"""
    new_json = json.dumps(my_obj)
    return new_json
