#!/usr/bin/python3
"""this 4-print_square.py Module for printa square
with the character #
suplies one function def print_square(size):"""


def print_square(size):
    """function that print a square with the character #"""
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for i in range(size):
        print("#" * size)


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/4-print_square.txt')
