#!/usr/bin/python3
def safe_print_division(a, b):
    res = 0
    try:
        res = a / b
        return (res)
    except ZeroDivisionError:

        return (None)
    finally:
        if res != 0:
            print("Inside result: {}".format(res))
        else:
            print("Inside result: {}".format(None))
