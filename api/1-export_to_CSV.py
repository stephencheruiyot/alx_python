import csv
import requests

def get_employee_info(employee_id):
    # Define API endpoints
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Fetch employee details
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    employee_name = employee_data.get("name")

    # Fetch TODO list
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Initialize counters
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for task in todos_data if task["completed"])

    # Create CSV file for the employee
    csv_file_name = f"{employee_id}.csv"

    with open(csv_file_name, mode="w", newline="") as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for task in todos_data:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": employee_name,
                "TASK_COMPLETED_STATUS": "Completed" if task["completed"] else "Not Completed",
                "TASK_TITLE": task["title"]
            })

    # Print progress information
    print("Employee {} is done with tasks ({}/{}):".format(employee_name, completed_tasks, total_tasks))
    for task in todos_data:
        if task["completed"]:
            print("\t {}".format(task["title"]))

if __name__ == "__main__":
    employee_id = int(input("Enter employee ID: "))
    get_employee_info(employee_id)
