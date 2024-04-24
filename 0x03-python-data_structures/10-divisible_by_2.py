#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    divisible_by_2 = []
    for y in my_list:
        divisible_by_2.append(y % 2 == 0)
    return (divisible_by_2)
