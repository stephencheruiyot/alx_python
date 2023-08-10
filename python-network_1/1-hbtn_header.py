"""
   A module that Sends a request to the given URL and displays the value of the X-Request-Id variable in the response header.

    Args:
        url (str): The URL to send the request to.

    Returns:
        str: The value of the X-Request-Id variable in the response header, or an error message.
    """

import requests
import sys

def get_request_id(url):
    """
    Send a request to the given URL and display the value of the X-Request-Id header.

    Args:
        url (str): The URL to send the request to.

    Returns:
        None
    """
    try:
        response = requests.get(url)
        x_request_id = response.headers.get('X-Request-Id')
        
        if x_request_id:
            print("X-Request-Id:", x_request_id)
        else:
            print("X-Request-Id not found in response headers.")
    except requests.exceptions.RequestException as e:
        print("Error:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <URL>")
        sys.exit(1)
    
    url = sys.argv[1]
    get_request_id(url)

