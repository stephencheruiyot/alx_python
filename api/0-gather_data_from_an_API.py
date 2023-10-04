#!/usr/bin/python3
"""
Retrieves and displays employee TODO list progress from a REST API
"""

import requests
import sys

# Base URLs for the API endpoints
users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"

def get_employee_info(employee_id):
    """Retrieve employee information and TODO list progress"""

    # Fetch employee details
    response_users = requests.get(f"{users_url}/{employee_id}")
    response_todos = requests.get(f"{todos_url}?userId={employee_id}")

    # Check if the employee exists
    if response_users.status_code != 200:
        print("Employee not found.")
        return

    user_data = response_users.json()
    employee_name = user_data.get('name')

    # Extract TODO list data
    todos_data = response_todos.json()
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for task in todos_data if task['completed'])

    # Display employee TODO list progress
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")

    # Display titles of completed tasks
    for task in todos_data:
        if task['completed']:
            print(f"\t{task['title']}")

if __name__ == "__main__":
    