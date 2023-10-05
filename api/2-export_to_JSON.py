'''
module that exports data to JSON and saves to  file

'''
import json
import requests
import sys

def get_employee_info(employee_id):
    # Define API endpoints
    base_url = "https://jsonplaceholder.typicode.com"
    user_endpoint = f"{base_url}/users/{employee_id}"
    todos_endpoint = f"{base_url}/users/{employee_id}/todos"

    # Get user details
    user_response = requests.get(user_endpoint)
    user_data = user_response.json()
    employee_name = user_data.get("name")

    # Get user's todo list
    todos_response = requests.get(todos_endpoint)
    todos_data = todos_response.json()

    # Count completed tasks and total tasks
    completed_tasks = [todo for todo in todos_data if todo["completed"]]
    total_tasks = len(todos_data)

    # Prepare the output format
    output = f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):"

    # Print the completed tasks
    for todo in completed_tasks:
        task_title = todo.get("title")
        output += f"\n\t{task_title}"

    # Print the output
    print(output)

    # Save the data to a JSON file
    user_info = {"USER_ID": [{"task": todo["title"], "completed": todo["completed"], "username": user_data["username"]} for todo in todos_data]}
    with open(f"{employee_id}.json", "w") as json_file:
        json.dump(user_info, json_file, indent=4)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
