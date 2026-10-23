#!/bin/bash
# Send a POST request with specific variables and display the response body.
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
