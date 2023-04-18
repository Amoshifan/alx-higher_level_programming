#!/usr/bin/python3
"""
Contains save_to_json_file() function
"""
import json


def save_to_json_file(my_obj, filename):
    """writes an Object to a text file, using a JSON representation"""
    with open(filename, "w", encoding="UTF8") as f:
        f.write(json.dumps(my_obj))
