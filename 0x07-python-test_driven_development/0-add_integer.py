#!/usr/bin/python3
"""Add two integers.

    Arguments:
    a -- first number (integer or float)
    b -- second number (integer or float), default is 98

    Returns:
    The sum of a and b, casted to integer.

    Raises:
    TypeError -- if a or b are not integers or floats
    """


def add_integer(a, b=98):
    if type(a) not in [int, float] or (a is None):
        raise TypeError("a must be an integer")
    if type(b) not in [int, float] or (b is None):
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b

