#!/usr/bin/python3

"""
Takes a script, sends a POST request to the passed URL
with the email as a parameter and displays the body of
the response(decoded in UTF 8)
"""

import urllib.request
import urllib.parse
import sys

if __name__ == "__main__":
    server_ip = sys.argv[1]
    email_add = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(email_add).encode("ascii")

    request = urllib.request.Request(server_ip, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
