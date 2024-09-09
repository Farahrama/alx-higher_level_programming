#!/usr/bin/python3
"""function that reads a text file (UTF8) and prints it to stdout:"""

def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout:"""
    try:
        with open(filename, encoding="UTF8") as file:
            print(file.read(), end="")
    except FileNotFoundError:
        print(f"[FileNotFoundError] [Errno 2] No such file or directory: 'file_nop'")
