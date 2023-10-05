import json
import requests


def get_employee_info(employee_id):
    # Define the base URL for the JSONPlaceholder API
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch employee details
    employee_url = f"{base_url}/users/{employee_id}"
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    employee_name = employee_data.get("name")

    # Fetch employee's todo list
    todo_url = f"{base_url}/users/{employee_id}/todos"
    todo_response = requests.get(todo_url)
    todo_data = todo_response.json()

    # Count completed and total tasks
    todos_done = sum(1 for todo in todo_data if todo["completed"])
    todos_count = len(todo_data)

    # Print the progress information
    print("Employee {} is done with tasks({}/{}):".format(employee_name, todos_done, todos_count))
    
    # Print the titles of completed tasks
    for todo in todo_data:
        if todo["completed"]:
            print("\t {}".format(todo["title"]))

    return {
        "user_id": employee_id,
        "tasks": [
            {"username": employee_name, "task": todo["title"], "completed": todo["completed"]}
            for todo in todo_data
        ]
    }

def export_to_json(employee_data):
    with open("todo_all_employees.json", "w") as json_file:
        json.dump(employee_data, json_file, indent=4)

if __name__ == "__main__":
    # Accept the employee ID as input
    employee_id = int(input("Enter an employee ID: "))
    
    # Get employee information and export to JSON
    employee_data = {employee_id: get_employee_info(employee_id)}
    export_to_json(employee_data)
