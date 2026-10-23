cat > README.md << 'EOF'
# python-network_0

Bash scripts that use `curl` to talk to a web server, plus a peak finder.

| File | Description |
|---|---|
| `0-body_size.sh` | Displays the size of the response body in bytes |
| `1-body.sh` | Displays the body of a 200 response |
| `2-delete.sh` | Sends a DELETE request and displays the body |
| `3-methods.sh` | Displays the HTTP methods the server accepts |
| `4-header.sh` | Sends the header `X-School-User-Id: 98` |
| `5-post_params.sh` | Sends a POST with `email` and `subject` variables |
| `6-peak.py`, `6-peak.txt` | Finds a peak in an unsorted list, O(log(n)) |
| `100-status_code.sh` | Displays only the status code of a response |
| `101-post_json.sh` | Sends the contents of a JSON file in a POST request |
| `102-catch_me.sh` | Makes the server answer with `You got me!` |
EOF
