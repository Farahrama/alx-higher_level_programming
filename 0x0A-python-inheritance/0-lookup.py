#!/usr/bin/python3
"""lookup function that returns the list of available attributes and methods"""


def lookup(obj):
    """return the list of available attributes and methods"""
    return dir(obj)
