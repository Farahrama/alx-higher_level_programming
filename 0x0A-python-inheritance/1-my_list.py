#!/usr/bin/python3
"""class MyList that inherits from list"""


class MyList(list):
    """Mylist class"""

    def print_sorted(self):
        """Print the list in sorted order"""
        sorted_list = sorted(self)
        print(sorted_list)


if __name__ == 'main':
    import doctest
    doctest.testfile('tests/1-my_list.txt')
