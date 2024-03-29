#!/usr/bin/python3
"""Takes a URL input and displays the value of X-Requst-Id"""
from urllib.request import urlopen
import sys

with urlopen(sys.argv[1]) as response:
    headers = response.info()
    for k, v in headers.items():
        if k == "X-Request-Id":
            print(v)
