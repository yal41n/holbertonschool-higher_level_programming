#!/usr/bin/python3
"""Search a user using the API and display the result"""
import requests
import sys

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    data = {"q": q}
    try:
        response = requests.post("http://0.0.0.0:5000/search_user", data=data)
        rjson = response.json()
        if rjson:
            print("[{}] {}".format(rjson.get("id"), rjson.get("name")))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
