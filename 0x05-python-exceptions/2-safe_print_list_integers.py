#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    cout = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end ="")
                cout += 1
        
        except IndexError:
            print("IndexError: list index out of range")
            break
    print()
    return cout