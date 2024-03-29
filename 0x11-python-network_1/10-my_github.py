#!/usr/bin/python3
"""Displays GitHub users ID."""
import requests
import sys

if __name__ == "__main__":
    url = 'https://api.github.com/' + sys.argv[1]
    header = {'Authorization': 'Bearer {}'.format(sys.argv[2])}
    response = requests.get(url, headers=header)
    print(response.json()['Id'])
