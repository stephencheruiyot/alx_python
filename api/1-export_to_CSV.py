import requests
import csv
import sys

def get_employee_info(employee_id):
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    response = requests.get(user_url)
    user_data = response.json()
    return user_data

def get_todo_list(employee_id):
    todo_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    response = requests.get(todo_url)
    todo_data = response.json()
    return todo_data

def export_to_csv(employee_id, user_info, todo_list):
    filename = f'{employee_id}.csv'
    with open(filename, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for task in todo_list:
            csv_writer.writerow([employee_id, user_info["username"], task["completed"], task["title"]])

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    
    employee_id = int(sys.argv[1])
    
    user_info = get_employee_info(employee_id)
    todo_list = get_todo_list(employee_id)
    
    completed_tasks = [task for task in todo_list if task["completed"]]
    total_tasks = len(todo_list)
    
    print("Employee {} is done with tasks({}/{})".format(
        user_info["name"],
        len(completed_tasks),
        total_tasks
    ))
    
    for task in completed_tasks:
        print("\t {}".format(task["title"]))
    
    export_to_csv(employee_id, user_info, todo_list)
    print(f"Data exported to {employee_id}.csv")
