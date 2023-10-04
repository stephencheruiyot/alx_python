import requests
import csv
import sys

def get_employee_info(employee_id):
    # Fetch employee details
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(user_url)
    user_data = response.json()
    employee_name = user_data.get("name")

    # Fetch TODO list for the employee
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(todo_url)
    todos = response.json()

    # Calculate progress
    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo["completed"])

    # Display progress
    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    for todo in todos:
        if todo["completed"]:
            print(f"\t{todo['title']}")

    # Export data to CSV
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos:
            csv_writer.writerow([employee_id, user_data["username"], todo["completed"], todo["title"]])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
