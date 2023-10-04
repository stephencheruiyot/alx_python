#!/usr/bin/python3
"""
Retrieve and export employee TODO list progress in CSV format
"""

import csv
import requests
import sys

# Constants for API endpoints
BASE_URL = "https://jsonplaceholder.typicode.com"
USERS_URL = BASE_URL + "/users/"
TODOS_URL = BASE_URL + "/todos"

def fetch_employee_info(employee_id):
    # Retrieve employee data
    user_response = requests.get(USERS_URL + str(employee_id))
    user_data = user_response.json()
    employee_name = user_data["name"]
    
    # Retrieve TODO list data for the employee
    todos_response = requests.get(TODOS_URL, params={"userId": employee_id})
    todos_data = todos_response.json()
    
    # Calculate progress
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo["completed"])
    
    # Print progress report
    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    
    # Print completed task titles and export to CSV
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        
        for todo in todos_data:
            task_title = todo["title"]
            task_status = "completed" if todo["completed"] else "not completed"
            csv_writer.writerow([employee_id, employee_name, task_status, task_title])
            if todo["completed"]:
                print(f"\t{task_title}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script_name.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_info(employee_id)
