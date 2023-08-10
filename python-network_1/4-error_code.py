#!/usr/bin/env python3

""" This script takes a URL as input, sends a request to the URL,
    and displays the response body. If the HTTP status code is
    greater than or equal to 400, it prints an error message
    with the HTTP status code.
"""

import requests
import sys

def main():
    """ Main function to execute the script
    """
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Print the response body
        print(response.text)

        # Check for HTTP status code >= 400
        if response.status_code >= 400:
            print(f"Error code: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
