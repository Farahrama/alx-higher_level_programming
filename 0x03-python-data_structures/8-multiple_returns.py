#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        sentence[:1] = ""
        return (len(sentence), sentence[:1])
    else:
        return (len(sentence), sentence[:1])
