#!/usr/bin/python3
""" HTTP Request Script
"""

import requests
import sys

def make_request(url):
    """ Sends a request to the given URL and displays the response body.

    Args:
        url (str): The URL to send the request to.

    Returns:
        None
    """
    try:
        response = requests.get(url)
        print(response.status_code)

        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")
    finally: 
        pass
    

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    make_request(url)
