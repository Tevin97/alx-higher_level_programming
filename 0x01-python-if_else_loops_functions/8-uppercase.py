#!/usr/bin/python3
def uppercase(s):
    for i in s:
        if ord(i) > 96 and ord(i) < 123:
            print("{:c}".format(ord(i) - 32), end="")
        else:
            print("{:c}".format(ord(i)), end="")
    print("")
