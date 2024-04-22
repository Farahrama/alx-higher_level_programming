#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == None:
        return None
    else:
        return(len(sentence), sentence[:1])
