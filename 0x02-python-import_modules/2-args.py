#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    num_args = len(args)

    print(f"{num_args}", end="")
    if num_args == 0:
        print(" arguments.")
    else:
        if num_args == 1:
            print(f" argument:", end="")
        else:
            print(" arguments:", end="")

        print()
        for i, arg in enumerate(args):
            print(f"{i+1}: {arg}")
