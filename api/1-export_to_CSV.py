import csv
import requests
import sys

def fetch_employee_info(employee_id):
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    try:
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()
        
        todos_response = requests.get(todos_url)
        todos_response.raise_for_status()
        todos_data = todos_response.json()
        
        return user_data, todos_data
    except requests.exceptions.HTTPError as e:
        print(f"Error fetching data: {e}")
        sys.exit(1)

def calculate_progress(user_data, todos_data):
    name = user_data.get("name")
    todos_done = sum(1 for todo in todos_data if todo.get("completed"))
    todos_count = len(todos_data)

    print(f"Employee {name} is done with tasks({todos_done}/{todos_count}):")
    
    completed_tasks = [todo.get("title") for todo in todos_data if todo.get("completed")]
    for task in completed_tasks:
        print(f"\t {task}")

def export_to_csv(user_data, todos_data):
    user_id = user_data.get("id")
    username = user_data.get("username")

    filename = f"{user_id}.csv"
    with open(filename, mode='w', newline='') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        
        for todo in todos_data:
            writer.writerow({
                'USER_ID': user_id,
                'USERNAME': username,
                'TASK_COMPLETED_STATUS': todo.get("completed"),
                'TASK_TITLE': todo.get("title")
            })

    print(f"Data exported to {filename}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)

    employee_id = int(sys.argv[1])
    user_data, todos_data = fetch_employee_info(employee_id)
    
    calculate_progress(user_data, todos_data)
    export_to_csv(user_data, todos_data)
