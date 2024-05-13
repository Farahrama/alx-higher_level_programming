#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_m = 0
    seen = set()
    for i in my_list:
        if i not in seen:
            sum_m += i
            seen.add(i)
    return sum_m
