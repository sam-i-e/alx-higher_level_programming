#!/usr/bin/python3
"""
Takes in a URL and sends a request to the URL and displays
the body of the response
Handles HTTP errors
"""

import urllib.error
import urllib.request
import sys

if __name__ == "__main__":
    server_ip = sys.argv[1]

    request = urllib.request.Request(server_ip)
    try:
        with urllib.request.urlopen(request) as response:
            print(response.read().decode("ascii"))
    except urllib.error.HTTPError as e:
        print("Error code: {}".format(e.code))
