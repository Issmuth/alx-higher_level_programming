#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    sum = 0
    argc = len(sys.argv)
    if argc > 1:
        for i in range(1, argc):
            sum = sum + int(sys.argv[i])

    print(sum)
