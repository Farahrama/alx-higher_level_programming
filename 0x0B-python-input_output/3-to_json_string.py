#!/usr/bin/python3
import json
"""function that returns the JSON representation of an object (string)"""
def to_json_string(my_obj):
    new_json = json.dumps(my_obj)
    return new_json