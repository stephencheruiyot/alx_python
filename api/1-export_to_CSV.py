import requests
import csv

def get_employee_todo_progress(employee_id):
    # Get employee details
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(user_url)
    employee_data = response.json()
    employee_name = employee_data.get("name")

    # Get employee's todo list
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(todo_url)
    todos = response.json()

    # Count completed tasks
    completed_tasks = [todo for todo in todos if todo.get("completed")]
    total_tasks = len(todos)
    completed_count = len(completed_tasks)

    # Display employee's TODO list progress
    print("Employee {} is done with tasks ({}/{}):".format(employee_name, completed_count, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task["title"]))

    # Export data to CSV
    export_to_csv(employee_id, employee_name, todos)

def export_to_csv(employee_id, employee_name, todos):
    csv_filename = f"{employee_id}.csv"
    with open(csv_filename, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos:
            writer.writerow([employee_id, employee_name, todo["completed"], todo["title"]])

if __name__ == "__main__":
    employee_id = int(input("Enter the employee ID: "))
    get_employee_todo_progress(employee_id)
