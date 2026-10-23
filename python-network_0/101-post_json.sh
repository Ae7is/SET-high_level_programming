#!/bin/bash
# Send a JSON POST request with a file's contents as the body.
curl -s -X POST -H "Content-Type: application/json" --data-binary @"$2" "$1"
