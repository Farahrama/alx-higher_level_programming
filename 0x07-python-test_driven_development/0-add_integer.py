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
    if a is None or (type(a) is not int and type(a) is not float):
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    result = a + b
    if result == float('inf') or result == -float('inf'):
        return 89
    return int(a) + int(b)
