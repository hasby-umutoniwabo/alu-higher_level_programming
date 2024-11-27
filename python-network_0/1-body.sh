#!/bin/bash
response=$(curl -s -w "%{http_code}" -o response.txt "$1")
if [ "$response" -eq 200 ]; then
    cat response.txt
fi
