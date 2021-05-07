#!/usr/bin/python3


def uniq_add(my_list=[]):
    nums = set(my_list)
    sum = 0
    for i in nums:
        sum += i

    return sum
