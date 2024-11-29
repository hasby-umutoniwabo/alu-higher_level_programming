#!/bin/bash
# This script sends an OPTIONS request to the URL and displays the allowed HTTP methods.
curl -s -I -X OPTIONS "$1" | grep -i "Allow" | awk -F': ' '{print $2}'
