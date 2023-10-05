import csv
import requests


def get_employee_info(employee_id):
    # Fetch employee details
    employee_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    response = requests.get(employee_url)
    employee_data = response.json()
    employee_name = employee_data.get('name')

    # Fetch TODO list for the employee
    todo_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"
    response = requests.get(todo_url)
    todos = response.json()

    # Calculate the number of completed and total tasks
    todos_done = sum(1 for todo in todos if todo['completed'])
    todos_count = len(todos)

    # Display employee TODO list progress
    print("Employee {} is done with tasks({}/{}):".format(employee_name, todos_done, todos_count))
    for todo in todos:
        if todo['completed']:
            print("\t", todo['title'])

    # Save data in CSV format
    with open(f"{employee_id}.csv", mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        for todo in todos:
            writer.writerow([employee_id, employee_name, todo['completed'], todo['title']])

if __name__ == "__main__":
    employee_id = int(input("Enter employee ID: "))
    get_employee_info(employee_id)
