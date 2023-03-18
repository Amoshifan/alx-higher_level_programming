#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    schl = []
    for key, valu in a_dictionary.items():
        if valu == value:
            schl.append(key)
    for key in schl:
        del a_dictionary[key]
    return(a_dictionary)
