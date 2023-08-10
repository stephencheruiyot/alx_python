#!/usr/bin/python3
"""
This script takes a letter as input and sends a POST request to http://0.0.0.0:5000/search_user.
The letter is sent as the parameter 'q'.
If no argument is given, 'q' is set to an empty string.
If the response body is properly JSON formatted and not empty, it displays the id and name in the format: [<id>] <name>.
Otherwise, it displays appropriate error messages.
Only the 'requests' and 'sys' packages are used.
"""

import requests
import sys

def main():
    """ Sends a POST request to http://0.0.0.0:5000/search_user and processes the response
    """
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": q}

    response = requests.post(url, data=data)
    try:
        response_json = response.json()
        
        if response_json:
            user_id = response_json.get("id")
            user_name = response_json.get("name")
            
            if user_id is not None and user_name is not None:
                print(f"[{user_id}] {user_name}")
            else:
                print("Not a valid JSON")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")

if __name__ == "__main__":
    main()
