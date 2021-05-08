#!/usr/bin/python3


def best_score(a_dictionary):
    max_n = 0
    max_k = None

    if a_dictionary:
        for k in a_dictionary:
            if a_dictionary[k] > max_n:
                max_k = k
                max_n = a_dictionary[k]

    return max_k
