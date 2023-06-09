#!/usr/bin/python3

import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    result = 0
    for i in args:
        result += int(i)
    print(result)
