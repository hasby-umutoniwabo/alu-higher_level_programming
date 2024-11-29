#!/bin/bash

# Check if URL is provided
if [ $# -eq 0 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# URL argument
URL=$1

# Send GET request with header and display the response body
curl -s -H "X-HolbertonSchool-User-Id: 98" "$URL"
