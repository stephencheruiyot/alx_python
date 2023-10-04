import requests
import json
import sys

def fetch_employee_todo_progress(employee_id):
    # Fetch employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()

    if 'name' not in employee_data:
        print(f"No employee found with ID {employee_id}")
        return

    employee_name = employee_data['name']

    # Fetch employee's TODO list
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # Count completed and total tasks
    completed_tasks = [task for task in todo_data if task['completed']]
    total_tasks = len(todo_data)

    # Display employee TODO list progress
    print(f"Employee {employee_name} is done with tasks ({len(completed_tasks)}/{total_tasks}):")
    for task in completed_tasks:
        print(f"\t{task['title']}")

    # Export data in JSON format
    all_employees_data = {}
    all_employees_data[employee_id] = [
        {
            "username": employee_data["username"],
            "task": task["title"],
            "completed": task["completed"]
        }
        for task in todo_data
    ]

    # Write data to todo_all_employees.json
    with open('todo_all_employees.json', 'a') as json_file:
        json.dump(all_employees_data, json_file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        fetch_employee_todo_progress(employee_id)
