#!/usr/bin/python3
"""Display the X-Request-Id header of the response of a URL."""
import requests
import sys

if __name__ == "__main__":
    response = requests.get(sys.argv[1])
    print(response.headers.get("X-Request-Id"))
