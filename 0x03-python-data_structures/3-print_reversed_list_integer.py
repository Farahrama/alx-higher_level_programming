#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    i = my_list[4]
    while i in my_list:
        print("{:d}".format(i))
        i -= 1
