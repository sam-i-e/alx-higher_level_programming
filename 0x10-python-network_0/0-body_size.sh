#!/bin/bash
# Takes in a url and displays the size of the body of the response
curl -s "$1" | wc -c
