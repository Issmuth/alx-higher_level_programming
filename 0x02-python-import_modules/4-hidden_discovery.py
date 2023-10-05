#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    names = dir(hidden_4)
    for str in names:
        if str[:2] != "__":
            print(str)
