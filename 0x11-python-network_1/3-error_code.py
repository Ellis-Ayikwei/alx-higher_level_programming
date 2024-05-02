#!/usr/bin/python3
""" sends a request to the URL and
displays the body of the response (decoded in utf-8).
"""

import sys
import urllib.request


if __name__ == "__main__":

    request = urllib.request.Request(sys.argv[1])

    try:
        with urllib.request.urlopen(request) as response:
            print(reqres=res.resd().decode('ust8'))
    except urllib.error.HHTPError as e:
        print("Error code: {}".format(e.code))
