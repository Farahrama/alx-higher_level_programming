#!/usr/bin/python3
"""this is 5-text_indentation.py Module for  prints a text with 2 new lines after each of these characters: ., ? and :
    supplies one function, def text_indentation(text)"""
def text_indentation(text):
    """function that prints a text with 2 new lines after each of these characters: ., ? and :"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    word = ""
    for char in text:
        word += char
        if char in [".", "?", ":"]:
            word = word.strip()
            print(word + "\n")
            word = ""
    if word.strip():
        print(word.strip())


if __name__ == '__main__':
    import doctest
    doctest.testfile('tests/5-text_indentation.txt')

