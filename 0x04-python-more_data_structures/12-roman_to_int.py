#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or not roman_string:
        return 0
    dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    init = 0
    before = 0
    total = 0
    for i in range(len(roman_string)):
        init = dict[roman_string[i]]
        if init > before:
            total = total + init - 2 * before
        else:
            total = total + init
        before = init
    return total
