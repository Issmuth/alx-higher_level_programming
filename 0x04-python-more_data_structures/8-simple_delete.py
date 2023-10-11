#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    key_list = list(a_dictionary)
    for i in key_list:
        if i == key:
            del a_dictionary[i]
    return a_dictionary
