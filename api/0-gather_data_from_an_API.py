#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: {} <employee_id>".format(sys.argv[0]))
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    # Step 1: Fetch employee information
    user_url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    user_response = requests.get(user_url)

    if user_response.status_code != 200:
        print("Employee not found.")
        sys.exit(1)

    user = user_response.json()
    employee_name = user.get("name")

    # Step 2: Fetch the employee's TODO list
    todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(employee_id)
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed") is True]
    num_done = len(done_tasks)

    # Step 3: Print the result in the required format
    print("Employee {} is done with tasks({}/{}):".format(employee_name, num_done, total_tasks))
    for task in done_tasks:
        print("\t {}".format(task.get("title")))

