#!/usr/bin/python3
for i in range(ord('z'), ord('a')-1, -1):
    if i % 2 == 0:
        print("{0}".format(chr(i)), end='')
    else:
        print("{0}".format(chr(i).upper()), end='')
