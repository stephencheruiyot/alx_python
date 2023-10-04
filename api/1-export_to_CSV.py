import csv
import requests


def get_employee_info(employee_id):
    # Define the base URL for the API
    base_url = "https://jsonplaceholder.typicode.com"

    # Create the URL for employee details
    employee_url = f"{base_url}/users/{employee_id}"

    # Make a GET request to fetch employee details
    employee_response = requests.get(employee_url)

    if employee_response.status_code != 200:
        print("Employee not found.")
        return

    employee_data = employee_response.json()
    employee_name = employee_data.get("name")

    # Create the URL for employee's TODO list
    todo_url = f"{base_url}/users/{employee_id}/todos"

    # Make a GET request to fetch TODO list
    todo_response = requests.get(todo_url)
    todo_list = todo_response.json()

    # Count completed tasks
    completed_tasks = [task for task in todo_list if task["completed"]]
    num_completed_tasks = len(completed_tasks)
    total_tasks = len(todo_list)

    # Print employee progress
    print(f"Employee {employee_name} is done with tasks ({num_completed_tasks}/{total_tasks}):")

    # Print completed tasks
    for task in completed_tasks:
        print(f"\t{task['title']}")

    # Export data to CSV
    user_id = employee_data.get("id")
    username = employee_data.get("username")
    csv_filename = f"{user_id}.csv"

    with open(csv_filename, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])

        for task in todo_list:
            csv_writer.writerow([user_id, username, task["completed"], task["title"]])

if __name__ == "__main__":
    employee_id = int(input("Enter Employee ID: "))
    get_employee_info(employee_id)
