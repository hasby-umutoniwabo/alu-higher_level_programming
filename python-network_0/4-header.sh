#!/bin/bash
<<<<<<< HEAD

# Check if URL is provided
if [ $# -eq 0 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# URL argument
URL=$1

# Send GET request with header and display the response body
curl -s -H "X-HolbertonSchool-User-Id: 98" "$URL"
=======
# This script sends a GET request to the URL with a custom header and displays the body of the response.
curl -s -H "X-HolbertonSchool-User-Id: 98" "$1"
>>>>>>> e716daa23763625784733288f27e8eb5843d8275
