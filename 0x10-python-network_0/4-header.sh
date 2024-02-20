#!/bin/bash

# Check if the script is provided with a URL argument
if [ $# -eq 0 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

# URL argument
url=$1

# Sending GET request with X-School-User-Id header
curl -X GET -H "X-School-User-Id: 98" "$url"
