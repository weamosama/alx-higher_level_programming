#!/usr/bin/python3

def uppercase(s):
    for char in s:
        if ord(char) >= ord('a') and ord(char) <= ord('z'):
            print("{:c}".format(ord(char) - 32), end="")
        else:
            print("{:c}".format(ord(char)), end="")
    print()
