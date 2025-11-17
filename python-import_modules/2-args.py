#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    count = len(sys.argv) - 1

    if count == 0:
        print("0 arguments.")
    else:
        print("{} argument{}:".format(count, "" if count == 1 else "s"))
        for i in range(1, len(sys.argv)):
            print("{}: {}".format(i, sys.argv[i]))
