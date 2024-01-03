#!/usr/bin/python3
"""
A script that fetches an employee's TODO list progress using a REST API
"""

import requests
import sys


def get_employee_todo_progress(employee_id):
    base_url = 'https://jsonplaceholder.typicode.com'
    todos_url = f'{base_url}/todos?userId={employee_id}'
    user_url = f'{base_url}/users/{employee_id}'

    try:
        response = requests.get(todos_url)
        response.raise_for_status()

        todos = response.json()
        user = requests.get(user_url).json()

        completed_tasks = [
                task['title']
                for task in todos
                if task['completed']
                ]
        num_completed_tasks = len(completed_tasks)
        total_tasks = len(todos)

        print(
                f"Employee {user['name']} "
                f"is done with tasks({num_completed_tasks}/{total_tasks}):"
                )
        for task in completed_tasks:
            print(f"\t{task['title']}")

    except requests.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    if not employee_id.isdigit():
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(int(employee_id))
