#!/usr/bin/python3
"""
This is the "5-test_indentation" module.
The 5-text_indentation module supplies one function, text_indentation(text).
"""


def text_indentation(text):
    """Splits a text into lines along "?", ":", "." followed by 2 new lines"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    flag = 0
    for char in text:
        if flag == 0:
            if char == ' ':
                continue
            else:
                flag = 1
        if flag == 1:
            if char in ['?', '.', ':']:
                print(char)
                print()
                flag = 0
            else:
                print(char, end="")


if __name__ == "__main__":
    text_indentation("Holberton. School? How are you: John")
