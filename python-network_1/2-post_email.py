"""
   A script that Sends a POST request to the given URL with the provided email as a parameter.
   
   Returns:
        str: The response body of the POST request.
"""

import sys
import requests

def send_post_request(url, email):
    """
    Sends a POST request to the given URL with the provided email as a parameter.

    Args:
        url (str): The URL to send the POST request to.
        email (str): The email address to be sent as a parameter.

    Returns:
        str: The response body of the POST request.
    """
    payload = {'email': email}
    response = requests.post(url, data=payload)
    return response.text

def main():
    """
    Main function that processes command line arguments and sends the POST request.
    """
    if len(sys.argv) != 3:
        print("Usage: {} <URL> <email>".format(sys.argv[0]))
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    print("Your email is:", email)
    
    response_body = send_post_request(url, email)
    print(response_body)

if __name__ == "__main__":
    main()
