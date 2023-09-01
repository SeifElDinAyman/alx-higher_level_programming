#!/usr/bin/python3
"""
This script fetches internet resources using the requests package.
It demonstrates how to make HTTP GET requests, decode the response,
and manipulate data from an external service.
"""

import requests

def fetch_url(url):
    """
    Fetches and prints the content of a URL.
    
    Args:
        url (str): The URL to fetch.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        content_type = response.headers.get('content-type', 'Unknown')
        
        print("Body response:")
        print(f"\t- type: {type(response.text)}")
        print(f"\t- content: {content_type}\n")
        print(response.text)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    url_to_fetch = 'https://alx-intranet.hbtn.io/status'
    fetch_url(url_to_fetch)

