#!/usr/bin/python3
"""Sends a request to the URL and displays a header."""
import requests
import sys


if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    header = response.headers.get('X-Request-Id')
    print(header)
