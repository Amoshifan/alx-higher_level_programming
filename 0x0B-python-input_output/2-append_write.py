#!/usr/bin/python3
"""
Contains append_file() function
"""


def append_write(filename="", text=""):
    """appends a string to a text file (UTF8)
     and returns the number of characters written"""
    with open(filename, "a", encoding="UTF8") as f:
        return f.write(text)

