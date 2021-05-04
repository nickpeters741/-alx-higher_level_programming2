#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        c = None
    return (len(sentence), sentence[:1])
