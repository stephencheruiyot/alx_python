#!/usr/bin/python3
"""
Retrieves and formats information about an employee's TODO list progress using a REST API and exports it in CSV format.
"""
import csv
import requests
import sys

def get_employee_info(employee_id):
    # Define API endpoints
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/users/{employee_id}/todos"

    # Fetch employee details
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get("name", "Unknown Employee")

    # Fetch TODO list
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Create a CSV file for the employee
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        
        # Write the CSV header
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        # Write each task to the CSV file
        for todo in todos_data:
            completed_status = "Completed" if todo["completed"] else "Not Completed"
            csv_writer.writerow([employee_id, employee_name, completed_status, todo["title"]])

    print(f"CSV file '{filename}' has been created.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
