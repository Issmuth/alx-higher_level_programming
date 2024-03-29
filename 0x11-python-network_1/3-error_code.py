#!/usr/bin/python3
"""Sends a request to a URL and displays the response."""
from urllib.request import urlopen
from urllib.error import HTTPError
import sys

if __name__ == "__main__":
    try:
        with urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except HTTPError as e:
        print('Error code: {}'.format(e.code))
