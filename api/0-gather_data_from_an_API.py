import requests

def fetch_employee_data(employee_id):
    employee_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todo_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    # Fetch employee data
    employee_response = requests.get(employee_url)
    employee_data = employee_response.json()
    employee_name = employee_data.get('name', 'Unknown Employee')

    # Fetch TODO list
    todo_response = requests.get(todo_url)
    todo_list = todo_response.json()

    # Calculate TODO list progress
    total_tasks = len(todo_list)
    completed_tasks = sum(1 for task in todo_list if task['completed'])

    # Display progress information
    print("Employee {} is done with tasks ({}/{}):".format(employee_name, completed_tasks, total_tasks))
    for task in todo_list:
        if task['completed']:
            print("\t{} ({})".format(task['title'], task['id']))

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
        fetch_employee_data(employee_id)
    except ValueError:
        print("Invalid employee ID. Please provide a valid integer.")
