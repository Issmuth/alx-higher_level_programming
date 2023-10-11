#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    key_list = list(a_dictionary)
    found = 0
    for i in key_list:
        if key == i:
            a_dictionary[i] = value
            found += 1
    if found == 0:
        a_dictionary[key] = value

    return a_dictionary
