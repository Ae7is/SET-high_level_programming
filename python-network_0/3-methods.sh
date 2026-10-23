#!/bin/bash
# Display all HTTP methods the server will accept using the OPTIONS method.
curl -sI -X OPTIONS "$1" | grep -i "Allow:" | cut -d ' ' -f 2- | tr -d '\r'
