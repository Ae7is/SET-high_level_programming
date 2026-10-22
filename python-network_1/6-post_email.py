#!/usr/bin/python3
"""Send a POST request with an email and display the response body."""
import requests
import sys

if __name__ == "__main__":
    response = requests.post(sys.argv[1], data={"email": sys.argv[2]})
    print(response.text)
