import requests
import csv
import sys

# Constants for API endpoints
TODO_API_URL = "https://jsonplaceholder.typicode.com/todos"
USER_API_URL = "https://jsonplaceholder.typicode.com/users"

def get_employee_info(employee_id):
    # Fetch employee data
    user_response = requests.get(f"{USER_API_URL}/{employee_id}")
    user_data = user_response.json()
    
    # Fetch todo list data for the employee
    todo_response = requests.get(f"{USER_API_URL}/{employee_id}/todos")
    todo_data = todo_response.json()
    
    return user_data, todo_data

def export_to_csv(employee_id, user_data, todo_data):
    # Create a CSV file with the employee_id as the filename
    filename = f"{employee_id}.csv"
    
    with open(filename, mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        # Write the CSV header
        writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"])
        
        # Write the todo list data to the CSV
        for todo in todo_data:
            writer.writerow([employee_id, user_data["username"], str(todo["completed"]), todo["title"]])

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    user_data, todo_data = get_employee_info(employee_id)

    # Calculate the number of completed and total tasks
    num_completed_tasks = sum(1 for todo in todo_data if todo["completed"])
    total_tasks = len(todo_data)

    # Print employee TODO list progress
    print(f"Employee {user_data['name']} is done with tasks ({num_completed_tasks}/{total_tasks}):")
    
    for todo in todo_data:
        if todo["completed"]:
            print(f"\t{todo['title']}")
    
    # Export data to CSV
    export_to_csv(employee_id, user_data, todo_data)

if __name__ == "__main__":
    main()
