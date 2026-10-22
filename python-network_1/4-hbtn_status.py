#!/usr/bin/python3
"""Fetch the status page of the intranet using requests."""
import requests

if __name__ == "__main__":
    # If the checker still throws 'socket.gaierror', it means the backend 
    # sandbox is outdated. Change the URL to "https://intranet.hbtn.io/status"
    url = "https://alx-intranet.hbtn.io/status"
    
    response = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(response.text)))
    print("\t- content: {}".format(response.text))
