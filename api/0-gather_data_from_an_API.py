import requests
import sys

# Define the base URL for the API
BASE_URL = "https://jsonplaceholder.typicode.com"

def fetch_employee_info(employee_id):
    try:
        # Fetch employee details
        employee_response = requests.get(f"{BASE_URL}/users/{employee_id}")
        employee_data = employee_response.json()
        employee_name = employee_data.get("name")

        # Fetch employee's TODO list
        todos_response = requests.get(f"{BASE_URL}/users/{employee_id}/todos")
        todos_data = todos_response.json()

        # Calculate TODO list progress
        total_tasks = len(todos_data)
        completed_tasks = sum(1 for todo in todos_data if todo.get("completed"))

        # Print the progress information
        print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
        
        # Print titles of completed tasks
        for todo in todos_data:
            if todo.get("completed"):
                print(f"\t{todo.get('title')}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    fetch_employee_info(employee_id)

if __name__ == "__main__":
    main()
