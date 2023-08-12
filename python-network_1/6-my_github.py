#!/usr/bin/env python3

"""
GitHub API User ID Display Script

This script takes GitHub credentials (username and personal access token) as arguments and uses the GitHub API to display the user's ID.
Only the 'read:user' permission is needed for this operation.

Usage:
    ./6-my_github.py <username> <personal_access_token>

Arguments:
    <username>          GitHub username
    <personal_access_token>   Personal access token for authentication

Example:
    ./6-my_github.py papamuziko cisfun
    Output: 2531536

    ./6-my_github.py papamuziko wrong_pwd
    Output: None
"""

import requests
import sys

def get_user_id(username, personal_access_token):
    
    """
    Get the user ID using GitHub API.

    Args:
        username (str): GitHub username
        personal_access_token (str): Personal access token for authentication

    Returns:
        str: User ID if successful, otherwise None
    """
    url = f'https://api.github.com/user'
    headers = {'Authorization': f'Bearer {personal_access_token}'}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        user_info = response.json()
        return str(user_info.get('id'))
    else:
        return None

def main():
    if len(sys.argv) != 3:
        print("Usage: ./6-my_github.py <username> <personal_access_token>")
        sys.exit(1)
    
    username = sys.argv[1]
    personal_access_token = sys.argv[2]
    
    user_id = get_user_id(username, personal_access_token)
    
    print(user_id)
    
    if user_id is not None:
        print(user_id)
    else:
        print("Error: Unable to fetch user ID")

if __name__ == "__main__":
    main()
