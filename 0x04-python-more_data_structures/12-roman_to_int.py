#!/usr/bin/python3


def roman_to_int(roman_string):
    '''
    Converts a Roman numeral to an integer
    '''
    new_num = 0
    i = 0
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
              'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}

    if roman_string and type(roman_string) == str:
        while i < len(roman_string):
            if i + 1 < len(roman_string) and roman_string[i:i + 2] in romans:
                new_num += romans[roman_string[i:i + 2]]
                i += 2
            else:
                new_num += romans[roman_string[i]]
                i += 1
        return new_num
    else:
        return new_num
