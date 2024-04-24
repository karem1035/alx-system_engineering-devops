#!/usr/bin/python3
"""A script that using a employee ID, returns information about his/her TODO"""

import requests
from sys import argv

if __name__ == "__main__":
    # Getting the employee id from the argument
    employee_id = argv[1]

    # Constructing URLs
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'{url}/todos'

    # Employee names
    employee_name = requests.get(url).json()['name']
    todos = requests.get(todos_url).json()
    completed = sum(1 for i in todos if i['completed'])

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
          completed, len(todos)))
    for i in todos:
        if i['completed']:
            print("\t {}".format(i['title']))
