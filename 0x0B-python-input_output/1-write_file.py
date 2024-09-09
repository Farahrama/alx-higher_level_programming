#!/usr/bin/python3
"""function that returns the number of characters written:"""
def write_file(filename="", text=""):
    try:
        with open(filename, encoding="UTF8") as file:
            print(file.write(text), end="")
    except FileNotFoundError:
        print(f"[FileNotFoundError] [Errno 2] No such file or directory: "
              f"'file_nop'")