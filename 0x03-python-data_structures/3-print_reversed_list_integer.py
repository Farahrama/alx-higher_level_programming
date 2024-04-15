#!/usr/bin/python3
def print_reversed_list_integer(my_list=None):
    if len(my_list) >= 5:
        i = len(my_list) - 1
        while i >= 0:
            print("{:d}".format(my_list[i]))
            i -= 1
