import csv
import requests


BASE_URL = "https://jsonplaceholder.typicode.com"

def fetch_employee_info(employee_id):
    employee_url = f"{BASE_URL}/users/{employee_id}"
    todos_url = f"{BASE_URL}/users/{employee_id}/todos"

    employee_response = requests.get(employee_url)
    todos_response = requests.get(todos_url)

    if employee_response.status_code != 200 or todos_response.status_code != 200:
        print("Error: Could not fetch employee data.")
        return None, []

    employee_data = employee_response.json()
    todos_data = todos_response.json()

    return employee_data, todos_data

def display_employee_progress(employee_id):
    employee_info, todos = fetch_employee_info(employee_id)

    if employee_info is None:
        return

    name = employee_info["name"]
    todos_count = len(todos)
    todos_done = sum(1 for todo in todos if todo["completed"])

    print("Employee {} is done with tasks({}/{}):".format(name, todos_done, todos_count))

    for todo in todos:
        if todo["completed"]:
            print("\t {}".format(todo["title"]))

def export_to_csv(employee_id):
    employee_info, todos = fetch_employee_info(employee_id)

    if employee_info is None:
        return

    user_id = employee_info["id"]
    username = employee_info["username"]
    filename = f"{user_id}.csv"

    with open(filename, mode='w', newline='') as csv_file:
        fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for todo in todos:
            writer.writerow({
                "USER_ID": user_id,
                "USERNAME": username,
                "TASK_COMPLETED_STATUS": todo["completed"],
                "TASK_TITLE": todo["title"]
            })

if __name__ == "__main__":
    employee_id = int(input("Enter the employee ID: "))
    
    display_employee_progress(employee_id)
    export_to_csv(employee_id)
