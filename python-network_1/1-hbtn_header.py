"""
   A module that Sends a request to the given URL and displays the value of the X-Request-Id variable in the response header.

    Args:
        url (str): The URL to send the request to.

    Returns:
        str: The value of the X-Request-Id variable in the response header, or an error message.
    """

import sys
import requests
"""
    Sends a request to the given URL and displays the value of the X-Request-Id variable in the response header.

    Args:
        url (str): The URL to send the request to.

    Returns:
        str: The value of the X-Request-Id variable in the response header, or an error message.
"""

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <url>")
        return

    url = sys.argv[1]
    response = requests.get(url)
    
    if response.status_code == 200:
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            print("X-Request-Id:", x_request_id)
        else:
            print("X-Request-Id header not found in the response.")
    else:
        print("Request failed with status code:", response.status_code)

if __name__ == "__main__":
    main()    
         