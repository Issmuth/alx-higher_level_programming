#!/usr/bin/python3
"""Takes a letter an sends a POST request to URL."""
import requests
import requests.exceptions
import sys

if __name__ == "__main__":
    data = {'q': ""}
    if len(sys.argv) > 1:
        data['q'] = sys.argv[1]
    response = requests.post('http://0.0.0.0:5000/search_user', data=data)
    try:
        rjson = response.json()
        if rjson == {}:
            print('No result')
        else:
            print('[{}] {}'.format(rjson['id'], rjson['name']))
    except ValueError as e:
        print("Not a valid JSON")
