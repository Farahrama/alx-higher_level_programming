#!/usr/bin/python3
def print_reversed_list_integer(my_list=None):
    if my_list is None:
        return
    if len(my_list) > 0:
        i = len(my_list) - 1
        while i >= 0:
            print("{:d}".format(my_list[i]))
            i -= 1
