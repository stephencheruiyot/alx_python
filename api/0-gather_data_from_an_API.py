#!/usr/bin/python3
"""
Retrieve information about an employee's TODO list progress from a REST API
"""

import requests
import sys

# Define the base URLs for the API endpoints
users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"

def get_employee_todo_progress(employee_id):
    """Retrieve and display employee's TODO list progress"""
    
    # Send a GET request to fetch the TODO list for the specified employee ID
    todos_response = requests.get(f"{users_url}/{employee_id}/todos")
    
    # Send a GET request to fetch employee details
    employee_response = requests.get(f"{users_url}/{employee_id}")
    
    # Check if the requests were successful
    if todos_response.status_code != 200 or employee_response.status_code != 200:
        print("Failed to fetch data from the API.")
        return
    
    # Parse the JSON responses
    todos_data = todos_response.json()
    employee_data = employee_response.json()
    
    # Extract relevant information
    employee_name = employee_data["name"]
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo["completed"])
    
    # Display the progress in the specified format
    print(f"Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):")
    
    # Display titles of completed tasks
    for todo in todos_data:
        if todo["completed"]:
            print(f"\t{todo['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
