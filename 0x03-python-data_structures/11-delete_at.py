#!/usr/bin/python3
def delete_At(my_list=[], idx=0):
    if idx < 0 or idx > len(my_list) - 1:
        return my_list
    new_list = []
    for i in range(len(my_list)):
        if i == idx:
            i += 1
        else:
            new_list.append(my_list[i])
    return new_list
