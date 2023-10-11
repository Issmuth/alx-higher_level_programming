#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return "None"
    key_list = list(a_dictionary)
    max = 0
    if len(key_list) == 0:
        return "None"
    for i in key_list:
        if a_dictionary[i] > max:
            max = a_dictionary[i]
            best = i
    return best
