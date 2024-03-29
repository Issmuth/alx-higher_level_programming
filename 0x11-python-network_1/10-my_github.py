#!/usr/bin/python3
"""Displays GitHub users ID."""
import requests
from requests.auth import HTTPBasicAuth
import sys

if __name__ == "__main__":
    authentication = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    response = requests.get('https://api.github.com/user', auth=authentication)
    print(response.json().get('id'))
