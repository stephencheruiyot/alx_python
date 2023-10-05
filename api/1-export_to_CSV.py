import csv
import os
import requests


# Base URL for the REST API
BASE_URL = "https://jsonplaceholder.typicode.com"

def get_employee_info(employee_id):
    # Get employee details
    user_url = f"{BASE_URL}/users/{employee_id}"
    user_response = requests.get(user_url)
    user_data = user_response.json()
    employee_name = user_data.get('name')

    # Get TODO list for the employee
    todos_url = f"{BASE_URL}/users/{employee_id}/todos"
    todos_response = requests.get(todos_url)
    todos_data = todos_response.json()

    # Calculate the progress
    total_tasks = len(todos_data)
    completed_tasks = sum(1 for todo in todos_data if todo['completed'])

    # Print employee progress in the specified format
    print("Employee {} is done with tasks({}/{}):".format(employee_name, completed_tasks, total_tasks))
    for todo in todos_data:
        if todo['completed']:
            print("\t {}".format(todo['title']))

    # Export data to CSV
    export_to_csv(employee_id, employee_name, todos_data)

def export_to_csv(employee_id, employee_name, todos_data):
    filename = f"{employee_id}.csv"
    with open(filename, mode='w', newline='') as csv_file:
        fieldnames = ['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

        for todo in todos_data:
            writer.writerow({
                'USER_ID': employee_id,
                'USERNAME': employee_name,
                'TASK_COMPLETED_STATUS': todo['completed'],
                'TASK_TITLE': todo['title']
            })

    print(f"Data exported to {filename}")

if __name__ == "__main__":
    try:
        employee_id = int(input("Enter an employee ID: "))
        get_employee_info(employee_id)
    except ValueError:
        print("Please enter a valid integer for the employee ID.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
