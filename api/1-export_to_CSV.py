import requests
import csv
import sys

def fetch_employee_data(employee_id):
    # Fetch employee details
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(user_url)
    user_data = response.json()
    
    # Fetch TODO list for the employee
    todos_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(todos_url)
    todos_data = response.json()
    
    return user_data, todos_data

def calculate_todo_progress(todos_data):
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo['completed'])
    return completed_tasks, total_tasks

def display_employee_progress(employee_name, completed_tasks, total_tasks, completed_task_titles):
    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    for task_title in completed_task_titles:
        print(f"\t{task_title}")

def export_to_csv(employee_id, employee_name, todos_data):
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        
        writer.writeheader()
        for todo in todos_data:
            writer.writerow({
                "USER_ID": employee_id,
                "USERNAME": employee_name,
                "TASK_COMPLETED_STATUS": todo["completed"],
                "TASK_TITLE": todo["title"]
            })

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    user_data, todos_data = fetch_employee_data(employee_id)
    employee_name = user_data["name"]
    completed_tasks, total_tasks = calculate_todo_progress(todos_data)
    completed_task_titles = [todo["title"] for todo in todos_data if todo["completed"]]
    
    display_employee_progress(employee_name, completed_tasks, total_tasks, completed_task_titles)
    export_to_csv(employee_id, employee_name, todos_data)
