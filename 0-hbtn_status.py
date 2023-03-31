#!/usr/bin/python3

"""Fetches https://alx-intranet.hbtn.io/status"""

import urllib.request

if __name__ == "__main__":
    link = 'https://alx-intranet.hbtn.io/status'
    with urllib.request.urlopen(link) as response:
        html = response.read()
        utf8_content = html.decode("UTF-8")
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(utf8_content))
