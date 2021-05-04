#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    cp = my_list[::-1]
    for i in cp:
        print("{:d}".format(i))
