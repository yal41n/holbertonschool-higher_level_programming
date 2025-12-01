#!/usr/bin/python3
"""Fetches a URL and prints the X-Request-Id from the header"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    headers = {"cfclearance": "true"}  # required for Holberton intranet
    response = requests.get(url, headers=headers)

    print(response.headers.get("X-Request-Id"))
