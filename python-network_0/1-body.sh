#!/bin/bash
# This script sends a GET request to the URL and displays the body if the status code is 200.
curl -sL "$1" -o temp_response.txt -w "%{http_code}" | grep -q "^200$" && cat temp_response.txt
