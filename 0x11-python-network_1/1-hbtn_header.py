#!/usr/bin/python3
"""Takes a URL input and displays the value of X-Requst-Id"""
from urllib.request import urlopen
import sys

if __name__ == "__main__":
    with urlopen(sys.argv[1]) as response:
        headers = response.info()
        print(headers.get('X-Request-Id'))
