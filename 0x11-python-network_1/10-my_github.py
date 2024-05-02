#!/usr/bin/python3
"""
    takes your GitHub credentials
    (username and password) and uses the GitHub API to display your id
"""
import requests
import sys

if __name__ == '__main__':

    r = requests.get('https://api.github.com/user',
                     auth=(sys.argv[1], sys.argv[2]))
    json = r.json()
    try:
        print(json['id'])
    except requests.exceptions.RequestException:
        print("None")
