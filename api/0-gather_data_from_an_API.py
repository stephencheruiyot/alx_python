#!/usr/bin/python3
"""
Retrieve and display employee TODO list progress from a REST API.
"""

import requests
import sys

# Base URLs for the API endpoints
users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"

def get_employee_todo_progress(employee_id):
    """
    Retrieve and display employee TODO list progress for a given employee ID.
    """
    # Send requests to fetch TODO list and user details
    todos_response = requests.get(f"{todos_url}?userId={employee_id}")
    user_response = requests.get(f"{users_url}/{employee_id}")

    # Check if requests were successful
    if todos_response.status_code != 200:
        print("Failed to fetch TODO list data.")
        sys.exit(1)

    if user_response.status_code != 200:
        print("Failed to fetch user data.")
        sys.exit(1)

    # Parse JSON responses
    todos_data = todos_response.json()
    user_data = user_response.json()

    # Calculate progress
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo["completed"])

    # Display progress information
    employee_name = user_data["name"]
    print("Employee {} is done with tasks({}/{}):".format(employee_name, completed_tasks, total_tasks))

    # Display titles of completed tasks
    for todo in todos_data:
        if todo["completed"]:
            print("\t {}".format(todo["title"]))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
    except ValueError:
        print("Invalid employee ID. Please provide a valid integer.")
        sys.exit(1)
