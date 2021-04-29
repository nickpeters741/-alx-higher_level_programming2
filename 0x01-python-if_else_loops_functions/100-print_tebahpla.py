#!/usr/bin/python3

n = 1
for i in range(26):
    if n % 2 == 0:
        let = chr(123 - n - 32)
    else:
        let = chr(123 - n)
    print("{}".format(let), end="")
    n  += 1
    if n
