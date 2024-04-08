#!/usr/bin/python3
alph = ""
for i in range(26):
    if i % 2 == 0:
        alph += chr(122 - i)
    else:
        alph += chr(90 - i)
print("{}".format(alph), end="")
