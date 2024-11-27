#!/bin/bash
# sends GET request to the URL provided as an arg displays body if 200
response=$(curl -s -w "%{http_code}" -o response.txt "$1")
if [ "$response" -eq 200 ]; then
    cat response.txt
fi
