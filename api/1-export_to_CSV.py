import csv
import os
import requests
import sys


# Base URL for the JSONPlaceholder API
BASE_URL = "https://jsonplaceholder.typicode.com"

def fetch_employee_data(employee_id):
    # Fetch employee details
    user_url = f"{BASE_URL}/users/{employee_id}"
    response = requests.get(user_url)
    user_data = response.json()
    username = user_data.get("username")

    # Fetch employee's TODO list
    todos_url = f"{BASE_URL}/users/{employee_id}/todos"
    response = requests.get(todos_url)
    todos_data = response.json()

    return username, todos_data

def main(employee_id):
    username, todos_data = fetch_employee_data(employee_id)

    # Calculate task progress
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo["completed"])

    # Display progress
    print("Employee {} is done with tasks ({}/{}):".format(username, completed_tasks, total_tasks))
    for todo in todos_data:
        if todo["completed"]:
            print("\t {}".format(todo["title"]))

    # Export data to CSV
    csv_filename = f"{employee_id}.csv"
    file_exists = os.path.exists(csv_filename)

    with open(csv_filename, "a", newline="") as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        if not file_exists:
            writer.writeheader()
        for todo in todos_data:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": username,
                "TASK_COMPLETED_STATUS": todo["completed"],
                "TASK_TITLE": todo["title"]
            })

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
    else:
        employee_id = int(sys.argv[1])
        main(employee_id)
