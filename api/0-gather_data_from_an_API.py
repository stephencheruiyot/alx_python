#!/usr/bin/python3
"""
Retrieves employee TODO list progress using a REST API
"""

import requests
import sys

users_url = "https://jsonplaceholder.typicode.com/users"
todos_url = "https://jsonplaceholder.typicode.com/users/{}/todos"

def get_employee_todo_progress(employee_id):
    try:
        # Fetch employee information
        user_response = requests.get(users_url + f'/{employee_id}')
        user_data = user_response.json()
        employee_name = user_data.get('name')

        # Fetch TODO list for the employee
        todo_response = requests.get(todos_url.format(employee_id))
        todo_data = todo_response.json()

        # Count completed and total tasks
        total_tasks = len(todo_data)
        completed_tasks = sum(1 for todo in todo_data if todo['completed'])

        # Print progress
        print(f'Employee {employee_name} is done with tasks({completed_tasks}/{total_tasks}):')

        # Print completed task titles
        for todo in todo_data:
            if todo['completed']:
                print(f'\t{todo["title"]}')
    
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except KeyError:
        print(f"Error: Employee with ID {employee_id} not found")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        get_employee_todo_progress(employee_id)
