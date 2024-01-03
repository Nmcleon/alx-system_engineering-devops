#!/user/bin/python3
"""
A sript that, uses a REST API, for a given employee ID, returns
information about his/her TODO list progress
and exports data in the JSON format.
"""

import json
import requests
from sys import argv


if __name__ == "__main__":

    session_request = requests.Session()

    emp_id = argv[1]
    baseurl = 'https://jsonplaceholder.typicode.com/users/{}/todos'.format(emp_id)
    urlName = 'https://jsonplaceholder.typicode.com/users/{}'.format(emp_id)

    employee = session_request.get(baseurl)
    employee_name = session_request.get(urlName)

    json_request = employee.json()
    user = employee_name.json()['username']

    total = []
    user_update = {}

    for all_Emp in json_request:
        total.append(
            {
                "task": all_Emp.get('title'),
                "completed": all_Emp.get('completed'),
                "username": user,
            })
    user_update[emp_id] = total

    file_Json = emp_id + ".json"
    with open(file_Json, 'w') as f:
        json.dump(user_update, f)
