import requests
import sys

def get_employee_todo_progress(employee_id):
    # Define the API endpoints
    base_url = "https://jsonplaceholder.typicode.com"
    todo_url = f"{base_url}/users/{employee_id}/todos"
    employee_url = f"{base_url}/users/{employee_id}"

    try:
        # Fetch employee data
        employee_response = requests.get(employee_url)
        employee_data = employee_response.json()
        employee_name = employee_data.get("name")

        # Fetch TODO list data
        todo_response = requests.get(todo_url)
        todo_data = todo_response.json()

        # Calculate TODO list progress
        total_tasks = len(todo_data)
        completed_tasks = sum(1 for task in todo_data if task["completed"])

        # Display progress information
        print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")

        # Display completed task titles
        for task in todo_data:
            if task["completed"]:
                print(f"\t{task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_todo_progress(employee_id)
