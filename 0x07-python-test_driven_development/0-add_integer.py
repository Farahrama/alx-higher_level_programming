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
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    try:
        result = a + b
        if result > sys.maxsize or result < -sys.maxsize - 1:
            raise OverflowError("Input too large to convert to integer")
    except OverflowError:
        raise OverflowError("Input too large to convert to integer")
    return result
