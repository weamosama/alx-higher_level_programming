#!/usr/bin/python3

def uppercase(s):
    result = ""
    for char in s:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            result += "{:c}".format(ord(char) - 32)
        else:
            result += "{:c}".format(ord(char))
    print(result)
