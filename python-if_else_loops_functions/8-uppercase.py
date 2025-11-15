#!/usr/bin/python3
def uppercase(str):
    res = ""
    for c in str:
        if 'a' <= c <= 'z':
            res += chr(ord(c) - 32)
        else:
            res += c
    print(res)
