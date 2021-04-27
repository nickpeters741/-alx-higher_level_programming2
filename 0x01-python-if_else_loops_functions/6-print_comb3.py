#!/usr/bin/python3
s = 0
for i in range(10):
    for n in range(s, 10):
        if i == n:
            continue
        print("{:d}{:d}".format(i, n), end=", ")
    s = s + 1
