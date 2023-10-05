import requests
import sys

def get_employee_data(employee_id):
    # Get employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(employee_url)
    employee_data = response.json()
    
    # Get TODO list for the employee
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(todos_url)
    todos = response.json()
    
    return employee_data, todos

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer")
        sys.exit(1)

    employee_data, todos = get_employee_data(employee_id)

    employee_name = employee_data.get("name")
    completed_tasks = [todo for todo in todos if todo["completed"]]
    total_tasks = len(todos)

    print("Employee {} is done with tasks ({}/{}):".format(
        employee_name,
        len(completed_tasks),
        total_tasks
    ))

    for task in completed_tasks:
        print("\t {}".format(task["title"]))

if __name__ == "__main__":
    main()
