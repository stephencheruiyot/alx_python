import sys
import requests

def get_x_request_id(url):
    """
    Sends a request to the given URL and displays the value of the X-Request-Id variable in the response header.

    Args:
        url (str): The URL to send the request to.

    Returns:
        str: The value of the X-Request-Id variable in the response header, or an error message.
    """
    try:
        response = requests.get(url)
        x_request_id = response.headers.get('X-Request-Id')
        if x_request_id:
            return f"X-Request-Id value: {x_request_id}"
        else:
            return "X-Request-Id not found in response header"
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

def main():
    """
    Main function to get URL from command-line arguments and call the get_x_request_id function.
    """
    if len(sys.argv) != 2:
        print("Usage: python script.py <url>")
        sys.exit(1)
    
    url = sys.argv[1]
    result = get_x_request_id(url)
    print(result)

if __name__ == "__main__":
    main()
