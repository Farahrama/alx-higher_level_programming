#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if len(my_list) >=5:
        i = len(my_list)
        while i > 0:
            print("{:d}".format(i))
            i -= 1
