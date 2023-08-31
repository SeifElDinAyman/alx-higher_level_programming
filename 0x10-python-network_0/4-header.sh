#!/bin/bash

if [ $# -ne 1 ]; then
  echo "Usage: $0 <URL>"
  exit 1
fi

url=$1
header="X-School-User-Id: 98"

response=$(curl -s -H "$header" "$url")
echo "$response"
