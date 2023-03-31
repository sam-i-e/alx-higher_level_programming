#!/usr/bin/python3
"""
Takes in a URL, sends a request to the URL and displays the
value of the variable X-Request-Id in the response header
"""

import sys
import requests

if __name__ == "__main__":
    server_ip = sys.argv[1]

    request = requests.get(server_ip)
    print(request.headers.get("X-Request-Id"))
