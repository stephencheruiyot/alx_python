import requests
import csv

# Constants
BASE_URL = "https://jsonplaceholder.typicode.com"
EMPLOYEE_ENDPOINT = BASE_URL + "/users/{employee_id}"
TODO_ENDPOINT = BASE_URL + "/users/{employee_id}/todos"
CSV_FILENAME = "{employee_id}.csv"

def get_employee_info(employee_id):
    # Get employee details
    response = requests.get(EMPLOYEE_ENDPOINT.format(employee_id=employee_id))
    employee_data = response.json()
    employee_name = employee_data.get("name")

    # Get employee's TODO list
    response = requests.get(TODO_ENDPOINT.format(employee_id=employee_id))
    todo_list = response.json()

    # Process TODO list
    total_tasks = len(todo_list)
    completed_tasks = [task for task in todo_list if task["completed"]]
    num_completed_tasks = len(completed_tasks)

    # Output employee information
    print("Employee {} is done with tasks ({}/{}):".format(
        employee_name, num_completed_tasks, total_tasks))
    
    # Output completed tasks
    for task in completed_tasks:
        print("\t{}".format(task["title"]))

    # Export data to CSV
    with open(CSV_FILENAME.format(employee_id=employee_id), mode="w", newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todo_list:
            writer.writerow([employee_id, employee_name, task["completed"], task["title"]])

if __name__ == "__main__":
    employee_id = int(input("Enter employee ID: "))
    get_employee_info(employee_id)
