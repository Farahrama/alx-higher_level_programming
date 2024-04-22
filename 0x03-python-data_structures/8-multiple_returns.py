#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        sentence = None
        return (len(sentence), sentence)
    else:
        return (len(sentence), sentence[:1])
