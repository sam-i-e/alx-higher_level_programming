#!/usr/bin/python3
"""
Takes in a URL and displays the value of X-Request-Id
"""

from urllib import request
from sys import argv

if __name__ == "__main__":
    if argv[1]:
        with request.urlopen(argv[1]) as response:
            print(response.getheader("X-Request-Id"))
