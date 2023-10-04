import requests
import sys

def get_employee_info(employee_id):
    # Define API endpoints
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/users/{employee_id}/todos"

    # Fetch employee information
    response = requests.get(user_url)
    employee_data = response.json()
    employee_name = employee_data.get("name")

    # Fetch TODO list
    response = requests.get(todos_url)
    todos_data = response.json()

    # Calculate progress
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo.get("completed"))

    # Display progress
    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    
    # Display completed tasks
    for todo in todos_data:
        if todo.get("completed"):
            print(f"\t{todo.get('title')}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    get_employee_info(employee_id)
