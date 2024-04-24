#!/usr/bin/python3
"""A script that using a employee ID, returns information about his/her TODO"""

import json
import requests
from sys import argv

if __name__ == "__main__":
    # Getting the employee id from the argument
    employee_id = argv[1]

    # Constructing URLs
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'{url}/todos'
    json_file = f'{employee_id}.json'

    # Employee names
    username = requests.get(url).json()['username']
    todos = requests.get(todos_url).json()
    array = []
    for i in todos:
        array.append(
            {
                "task": i['title'],
                "completed": i['completed'],
                "username": username
            }
        )
    with open(json_file, "w") as file:
        json.dump({
            employee_id: array
        }, file)
