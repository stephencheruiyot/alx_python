import csv
import requests
import sys
import os

# Define the base URL for the API
BASE_URL = "https://jsonplaceholder.typicode.com"

def get_employee_info(employee_id):
    # Fetch employee details
    employee_url = f"{BASE_URL}/users/{employee_id}"
    response = requests.get(employee_url)
    employee_data = response.json()
    
    if not employee_data:
        print("Employee not found.")
        return None
    
    employee_name = employee_data.get("name")

    # Fetch TODO list for the employee
    todo_url = f"{BASE_URL}/users/{employee_id}/todos"
    response = requests.get(todo_url)
    todos = response.json()

    return employee_name, todos

def export_to_csv(employee_id, employee_name, todos):
    if not todos:
        return

    filename = f"{employee_id}.csv"
    
    with open(filename, mode="w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file, quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        
        for todo in todos:
            csv_writer.writerow([employee_id, employee_name, todo["completed"], todo["title"]])

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <employee_id>")
        sys.exit(1)
    
    employee_id = sys.argv[1]

    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    employee_info = get_employee_info(employee_id)
    
    if employee_info:
        employee_name, todos = employee_info
        total_tasks = len(todos)
        completed_tasks = sum(1 for todo in todos if todo["completed"])
        
        print("Employee {} is done with tasks({}/{}):".format(
            employee_name, completed_tasks, total_tasks))
        
        for todo in todos:
            if todo["completed"]:
                print("\t {}".format(todo["title"]))
        
        export_to_csv(employee_id, employee_name, todos)
        if os.path.exists(f"{employee_id}.csv"):
            print(f"Data exported to {employee_id}.csv")
        else:
            print(f"No CSV file found for employee {employee_id}.")

if __name__ == "__main__":
    main()
