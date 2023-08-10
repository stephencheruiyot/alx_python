#!/usr/bin/python3
"""
Sends a request to a URL and displays the value of the variable X-Request-Id in the response header.
Uses the requests and sys packages only.
"""

import sys
import requests

def main():
    if len(sys.argv) != 2:
        print("Usage: {} <URL>".format(sys.argv[0]))
        sys.exit(1)
    
    url = sys.argv[1]
    
    try:
        response = requests.get(url)
        x_request_id = response.headers.get('X-Request-Id')
        
        if x_request_id:
            print(x_request_id)
        else:
            print("None")
            
    except requests.RequestException as e:
        print("An error occurred: {}".format(e))

if __name__ == "__main__":
    main()
