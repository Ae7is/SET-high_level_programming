#!/bin/bash
# Send a GET request with a custom custom header and display the body.
curl -sH "X-School-User-Id: 98" "$1"
