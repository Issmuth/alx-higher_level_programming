#!/usr/bin/python3
"""Fetches from URL."""
from urllib.request import urlopen


with urlopen('https://alx-intranet.hbtn.io/status') as s:
    response = {}
    response['type'] = type(s)
    response['content'] = s.read()
    response['utf8 content'] = response['content'].decode('utf-8')
    print('Body response:')
    for k,v in response.items():
        print("    - {}: {}".format(k, v))
