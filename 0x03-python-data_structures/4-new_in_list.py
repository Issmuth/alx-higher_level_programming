#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    size = len(my_list)
    if idx < 0 or idx > size - 1:
        return my_list

    new_list = []
    for i in range(size):
        if i == idx:
            new_list.append(element)
            i += 1
        else:
            new_list.append(my_list[i])

    return new_list
