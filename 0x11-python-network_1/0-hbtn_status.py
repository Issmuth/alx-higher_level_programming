#!/usr/bin/python3
"""Fetches from URL."""
from urllib.request import urlopen


with urlopen('https://alx-intranet.hbtn.io/status') as s:
    response = {}
    content = s.read()
    response['type'] = type(content)
    response['content'] = content
    response['utf8 content'] = content.decode('utf-8')
    print('Body response:')
    for k, v in response.items():
        print("i\t- {}: {}".format(k, v))
