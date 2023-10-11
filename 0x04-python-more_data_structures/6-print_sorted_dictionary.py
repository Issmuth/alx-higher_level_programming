#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary): 
    s_dictionary = sorted(a_dictionary)
    for i in s_dictionary:
        print(i + ": ", a_dictionary[i])
