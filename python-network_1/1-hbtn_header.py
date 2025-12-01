#!/usr/bin/python3
"""Fetches a URL and displays the X-Request-Id header value"""
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    req = urllib.request.Request(url)

    with urllib.request.urlopen(req) as response:
        # Get headers as a dict-like object
        headers = response.headers

        # Display the X-Request-Id header using get()
        print(headers.get("X-Request-Id"))
