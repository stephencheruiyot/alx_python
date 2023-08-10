"""
    Main function that takes a URL as input, sends a request to the URL,
    and displays the body of the response. If the HTTP status code is
    greater than or equal to 400, it prints an error message with the
    status code.

    Usage: python 4-error_code.py <URL>
"""

import requests
import sys

def main():
    """
    Main function that takes a URL as input, sends a request to the URL,
    and displays the body of the response. If the HTTP status code is
    greater than or equal to 400, it prints an error message with the
    status code.

    Usage: python 4-error_code.py <URL>
    """
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python 4-error_code.py <URL>")
        sys.exit(1)
    
    url = sys.argv[1]  # Get the URL from command-line arguments

    try:
        response = requests.get(url)  # Send a GET request to the URL

        if response.status_code >= 400:
            # If the status code is 400 or higher, print an error message
            print(f"Error code: {response.status_code}")
        else:
            # If the status code is less than 400, print the response body
            print(response.text)
    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
