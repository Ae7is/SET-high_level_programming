#!/usr/bin/python3
"""Search a user by letter using a POST request and display the result."""
import requests
import sys

if __name__ == "__main__":
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    url = "http://0.0.0.0:5000/search_user"
    response = requests.post(url, data={"q": letter})
    try:
        data = response.json()
        if not data:
            print("No result")
        else:
            print("[{}] {}".format(data.get("id"), data.get("name")))
    except ValueError:
        print("Not a valid JSON")
