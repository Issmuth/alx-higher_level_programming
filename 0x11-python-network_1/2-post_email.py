#!/usr/bin/python3
"""Sends a POST requset to a URL with an email."""
from urllib.request import urlopen, Request
from urllib.parse import urlencode
import sys

if __name__ == "__main__":
    data = {'email': sys.argv[2]}
    data = urlencode(data)
    data = data.encode('ascii')

    r = Request(sys.argv[1], data)
    with urlopen(r) as post:
        print(post.read().decode('utf-8'))
