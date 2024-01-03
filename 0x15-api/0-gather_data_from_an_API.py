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
    base_url = 'https://jsonplaceholder.typicode.com/users/{}/todos'
    .format(employee_id)
    url_name = 'https://jsonplaceholder.typicode.com/users/{}'
    .format(employee_id)

    employee = sessionReq.get(base_url)
    employee_name = sessionReq.get(url_name)

    json_request = employee.json()
    name = employee_name.json()['name']

    totalTasks = 0

    for completed_tasks in json_request:
        if completed_tasks['completed']:
            totalTasks += 1

    print("Employee {} is done with tasks({}/{}):".
          format(name, totalTasks, len(json_request)))

    for completed_tasks in json_request:
        if completed_tasks['completed']:
            print("\t " + completed_tasks.get('title'))
