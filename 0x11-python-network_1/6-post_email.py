#!/usr/bin/python3
"""Sends a POST request to URL with email."""
import requests
import sys

if __name__ == "__main__":
    data = {'email': sys.argv[2]}
    response = request.post(sys.argv[1], data=data)
    print(response)
