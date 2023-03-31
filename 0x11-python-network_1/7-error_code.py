#!/usr/bin/python3
"""
Sends a request to a URL and displays the response body
Handles errors
"""

import sys
import requests

if __name__ == "__main__":
    server_ip = sys.argv[1]

    r = requests.get(server_ip)
    if r.status_code >= 400:
        print("Error code: {}".format(r.status_code))
    else:
        print(r.text)
