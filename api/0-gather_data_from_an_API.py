import requests
import sys

def get_employee_info(employee_id):
    # Define the API endpoints
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Send requests to the API
    employee_response = requests.get(employee_url)
    todos_response = requests.get(todos_url)

    # Check if the requests were successful
    if employee_response.status_code != 200 or todos_response.status_code != 200:
        print("Failed to fetch data from the API")
        return

    # Parse JSON responses
    employee_data = employee_response.json()
    todos_data = todos_response.json()

    # Extract relevant information
    employee_name = employee_data.get("name")
    completed_tasks = [task for task in todos_data if task["completed"]]
    total_tasks = len(todos_data)
    completed_count = len(completed_tasks)

    # Print employee TODO list progress
    print("Employee {} is done with tasks({}/{}):".format(employee_name, completed_count, total_tasks))
    for task in completed_tasks:
        print("\t {}".format(task["title"]))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        get_employee_info(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
