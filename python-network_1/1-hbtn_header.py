#!/usr/bin/python3
"""Display the X-Request-Id header of the response of a URL."""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers.get("X-Request-Id"))
