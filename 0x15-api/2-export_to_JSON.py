#!/usr/bin/python3
"""
A script that fetches an employee's TODO list progress using a REST API
and exports data in JSON format.
"""

import json
import requests
from sys import argv

def export_to_json(employee_id):
    base_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}/todos'
    user_url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'

    try:
        response_todos = requests.get(base_url)
        response_user = requests.get(user_url)

        response_todos.raise_for_status()
        response_user.raise_for_status()

        todos_data = response_todos.json()
        user_data = response_user.json()

        user_name = user_data['name']
        user_id = str(user_data['id'])
        tasks = [{"task": task['title'], "completed": task['completed'], "username": user_name} for task in todos_data]

        json_output = {user_id: tasks}
        file_name = f"{user_id}.json"

        with open(file_name, 'w') as json_file:
            json.dump(json_output, json_file, indent=4)

        print(f"Data exported to {file_name}")

    except requests.RequestException as e:
        print(f"Error: {e}")
        exit(1)

if __name__ == "__main__":
    if len(argv) != 2:
        print("Usage: python3 script_name.py <employee_id>")
        exit(1)

    employee_id = argv[1]

    if not employee_id.isdigit():
        print("Employee ID must be an integer.")
        exit(1)

    export_to_json(int(employee_id))
