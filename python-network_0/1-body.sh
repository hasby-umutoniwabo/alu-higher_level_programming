#!/bin/bash
# This script sends a GET request to the URL and displays the body if the status code is 200.
response=$(curl -s -w "%{http_code}" -o temp_response.txt "$1")
[ "$response" -eq 200 ] && cat temp_response.txt
