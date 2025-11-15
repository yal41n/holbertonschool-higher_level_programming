#!/usr/bin/python3
def uppercase(str):
    result = ""
    for char in str:
        # If character is lowercase a-z, convert to uppercase by subtracting 32
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))

