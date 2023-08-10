#!/usr/bin/python3
""" Script to send a request to a URL and display the response body or error code
"""
import requests
import sys

def main():
    """ Main function to perform the request and handle the response
    """
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    response = requests.get(url)

    if response.status_code >= 400:
        print("Error code:", response.status_code)
    
        

if __name__ == "__main__":
    main()
