#!/usr/bin/python3
"""Send a POST request with an email parameter and display the response body"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {"email": email}
    response = requests.post(url, data=data)
    print(response.text)
