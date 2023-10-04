import csv
import requests

def fetch_employee_data(employee_id):
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("Error: Unable to fetch data.")
        return None, None

    user_data = user_response.json()
    todos_data = todos_response.json()

    return user_data, todos_data

def calculate_todo_progress(user_data, todos_data):
    employee_name = user_data.get('name')
    total_tasks = len(todos_data)
    done_tasks = sum(1 for todo in todos_data if todo['completed'])

    return employee_name, done_tasks, total_tasks, todos_data

def display_todo_progress(employee_name, done_tasks, total_tasks, todos_data):
    print("Employee {} is done with tasks ({}/{}):".format(employee_name, done_tasks, total_tasks))
    
    for todo in todos_data:
        if todo['completed']:
            print("\t {}".format(todo['title']))

def export_to_csv(employee_id, user_data, todos_data):
    csv_file_name = f"{employee_id}.csv"
    
    with open(csv_file_name, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        
        for todo in todos_data:
            csv_writer.writerow([user_data['id'], user_data['username'], todo['completed'], todo['title']])

if __name__ == "__main__":
    employee_id = int(input("Enter the employee ID: "))
    
    user_data, todos_data = fetch_employee_data(employee_id)
    
    if user_data and todos_data:
        employee_name, done_tasks, total_tasks, todos_data = calculate_todo_progress(user_data, todos_data)
        display_todo_progress(employee_name, done_tasks, total_tasks, todos_data)
        export_to_csv(employee_id, user_data, todos_data)
