#!/usr/bin/python3
"""function that appends a string at the end of a text file (UTF8)"""


def append_write(filename="", text=""):
    """returns the number of characters added"""
    with open(filename, "a", encoding="UTF8") as file:
        return file.write(text)
