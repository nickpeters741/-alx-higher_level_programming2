#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    count = 0
    cp = my_list[:]
    if idx < 0 or idx > len(my_list):
        return cp
    for i in cp:
        if count == idx:
            cp[idx] = element
        count += 1

    return cp
