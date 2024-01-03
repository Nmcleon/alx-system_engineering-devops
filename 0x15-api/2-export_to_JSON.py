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
    usr = employee_name.json()['username']

    total = []
    user_update = {}

    for all_Emp in json_request:
        total.append(
            {
                "task": all_Emp.get('title'),
                "completed": all_Emp.get('completed'),
                "username": usr,
            })
    user_update[empid] = total

    file_Json = empid + ".json"
    with open(file_Json, 'w') as f:
        json.dump(user_update, f)
