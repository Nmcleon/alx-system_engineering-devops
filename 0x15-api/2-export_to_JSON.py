#!/usr/bin/python3
"""
A script that fetches an employee's TODO list progress using a REST API
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    sessionReq = requests.Session()

    employee_id = argv[1]
    base_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(employee_id)
    url_name  = 'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)

    employee = sessionReq.get(base_url)
    employee_name = sessionReq.get(url_name)

    json_request = employee.json()
    name = employee_name.json()['name']

    totalTasks = []
    user_update = {}

    for completed_tasks in json_request:
        totalTask.append(
            {
                "task": completed_tasks.get('title'),
                "completed": completed_tasks.get('completed'),
                "username": user,
            })
        user_update[employee_id] = totalTasks

        file_Json = employee_id + ".json"
        with open(file_Json, 'w') as f:
            json.dump(user_update, f)
