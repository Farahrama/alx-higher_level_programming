#!/usr/bin/python3
"""function that returns the dictionary description with simple
 data structure (list, dictionary, string, integer and boolean)
   for JSON serialization"""


def class_to_json(obj):
    """hat returns the dictionary description with simple
 data structure """
    return obj.__dict__
