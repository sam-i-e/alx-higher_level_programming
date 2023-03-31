#!/usr/bin/python3
"""
Sends a POST request to a given URL with a given letter
The letter is sent as the value of the variable 'q'
if no letter is provided, sends  q=""
"""

import sys
import requests


if __name__ == "__main__":
    letter = "" if len(sys.argv) == 1 else sys.argv[1]
    lval = {"q": letter}

    r = requests.post("http://0.0.0.0:5000/search_user", data=lval)
    try:
        response = r.json()
        if response == {}:
            print("No result")
        else:
            print("[{}] {}".format(response.get("id"), response.get("name")))
    except ValueError:
        print("Not a valid JSON")
