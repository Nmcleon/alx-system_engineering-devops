#!/usr/bin/python3
"""
A script that fetches an employee's TODO list progress using a REST API
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    session_request = requests.Session()

    empid = argv[1]
    base = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(empid)
    urlName = 'https://jsonplaceholder.typicode.com/users/{}'.format(empid)

    employee = session_request.get(base)
    employee_name = session_request.get(urlName)

    json_request = employee.json()
    name = employee_name.json()['name']

    total = 0

    for completed_task in json_request:
        if completed_task['completed']:
            total += 1

    print("Employee {} is done with tasks({}/{}):".
          format(name, total, len(json_request)))

    for completed_task in json_request:
        if completed_task['completed']:
            print("\t " + completed_task.get('title'))
