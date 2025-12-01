#!/usr/bin/python3
"""Fetch and display the GitHub user ID using Basic Authentication"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = "https://api.github.com/user"
    response = requests.get(url, auth=(username, token))
    try:
        print(response.json().get("id"))
    except Exception:
        print("None")
