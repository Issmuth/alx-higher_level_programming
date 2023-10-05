#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argc = len(sys.argv)
    if argc == 1:
        print("0 argmuents.")
    elif argc == 2:
        print("1 argument:\n1: {}".format(sys.argv[1]))
    else:
        print("{} arguments:".format(argc))
        for i in range(1, argc):
            print("{}: {}".format(i, sys.argv[i]))
