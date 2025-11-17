#!/usr/bin/python3
"""Function that returns the length of a string and its first character"""


def multiple_returns(sentence):
    if not sentence:
        return (0, None)
    return (len(sentence), sentence[0])
