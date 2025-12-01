#!/usr/bin/python3
"""Sends a POST request with an email parameter and displays the response"""
import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Prepare the POST data
    data = urllib.parse.urlencode({"email": email}).encode("utf-8")

    # Create the request
    req = urllib.request.Request(url, data=data)

    # Send request using with statement
    with urllib.request.urlopen(req) as response:
        body = response.read().decode("utf-8")
        print(body)
