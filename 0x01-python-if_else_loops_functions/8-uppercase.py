#!/usr/bin/python3
def uppercase(s):
    for i in s:
        if ord(i) > 96 and ord(i) < 123:
            i = chr(ord(i) - 32)
        print("{}".format(i), end="")
    print("")
