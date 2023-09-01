#!/usr/bin/python3
"""A script that
- takes in a URL
- sends a request to the URL
- displays the body of the response.
"""
import requests

if __name__ == "__main__":
    url = sys.argv[1]
    
	url = 'https://alx-intranet.hbtn.io/status'
	response = requests.get(url)

	print("Body response:")
	print("\t- type:", type(response.text))
	print("\t- content:", response.text)
