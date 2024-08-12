#!/usr/bin/python3
"""this is 3-say_my_name.py Module for print fist and second name
suplies one function, def say_my_name(first_name, last_name="")
"""


def say_my_name(first_name, last_name=""):
    """function that prints My name is <first name> <last name> """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile('tests/3-say_my_name.txt')
