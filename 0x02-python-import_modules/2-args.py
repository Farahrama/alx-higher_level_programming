#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    c = len(sys.argv) - 1
    if c == 0:
        print("0 arguments.")
    else:
        print("{} arguments:".format(c))
    for i in range(c):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
