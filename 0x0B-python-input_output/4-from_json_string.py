#!/usr/bin/python3
"""function that returns an object (Python data structure) represented by a JSON string"""
import json


def from_json_string(my_str):
    new_json = json.loads(my_str)
    return new_json
