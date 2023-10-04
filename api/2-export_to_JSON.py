"""
Employee Progress Module

This module provides functions to retrieve and analyze employee progress based on their
TODO list from a JSON API. It fetches the employee's tasks, counts completed tasks, and
exports completed tasks to a JSON file.

Usage:
    $ python script.py <employee_id>

Author: stephen cheruiyot
"""
import json
import requests
import sys

def get_employee_todo_progress(employee_id):
    # Define the API endpoints
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    try:
        # Fetch employee TODO list
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        # Fetch employee details
        user_response = requests.get(user_url)
        user_data = user_response.json()

        # Count completed and total tasks
        total_tasks = len(todo_data)
        completed_tasks = sum(1 for task in todo_data if task['completed'])

        # Display employee TODO list progress
        print(f"Employee {user_data['name']} is done with tasks ({completed_tasks}/{total_tasks}):")

        # Display completed tasks and record them in a list
        completed_task_list = []
        for task in todo_data:
            if task['completed']:
                print(f"\t{task['title']}")
                completed_task_list.append({"task": task['title'], "completed": True, "username": user_data['username']})

        # Export completed tasks to a JSON file
        with open(f"{employee_id}.json", "w") as json_file:
            json.dump({user_data['id']: completed_task_list}, json_file, indent=4)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
