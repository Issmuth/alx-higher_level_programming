#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        return (0, "None")
    ret = len(sentence), sentence[0]
    return ret
