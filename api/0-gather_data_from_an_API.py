#!/usr/bin/python3
"""
Checks student output for returning information from a REST API
"""

import requests
import sys

# URLs for the REST API endpoints
users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/todos"

def check_tasks(employee_id):
    """Fetch user name and check formatting of tasks"""

    try:
        # Fetch user data from the REST API
        user_data = requests.get(users_url + f'/{employee_id}').json()
        employee_name = user_data.get('name')

        # Fetch task data from the REST API
        task_data = requests.get(todos_url).json()

        # Initialize variables to count tasks and track formatting
        filename = 'student_output'
        count = 0

        with open(filename, 'r') as f:
            next(f)  # Skip the header line
            for line in f:
                count += 1
                if line[0] == '\t' and line[1] == ' ' and line[-1] == '\n':
                    print(f"Task {count} Formatting: OK")
                else:
                    print(f"Task {count} Formatting: Incorrect")

        # Print user information
        print(f"Employee {employee_name} tasks checked")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except KeyError:
        print(f"Error: Employee with ID {employee_id} not found")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        check_tasks(employee_id)
