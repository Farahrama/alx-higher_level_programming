#!/usr/bin/python3
"""function that returns an object Python represented by a JSON string"""
import json


def from_json_string(my_str):
    """returns an object Python represented by a JSON string"""
    new_json = json.loads(my_str)
    return new_json
