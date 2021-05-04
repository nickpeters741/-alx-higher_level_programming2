#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        c = None
    c = sentence[:1]
    return (len(sentence), c)
