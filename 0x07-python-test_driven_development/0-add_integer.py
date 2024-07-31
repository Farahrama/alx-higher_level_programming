#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers or floats after converting them to integers.

    Parameters:
    a (int or float): The first number to add.
    b (int or float, optional): The second number to add. Defaults to 98.

    Returns:
    int: The sum of a and b after converting them to integers.

    Raises:
    TypeError: If a or b are not integers or floats.
    """
    if type(a) not in [int, float] or (a is None):
        raise TypeError("a must be an integer")
    if type(b) not in [int, float] or (b is None):
        raise TypeError("b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    result = a + b
    if result > sys.maxsize or result < -sys.maxsize - 1:
        raise OverflowError("Input too large to convert to integer")
    return result

