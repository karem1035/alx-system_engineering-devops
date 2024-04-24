#!/usr/bin/python3
# A script that using a employee ID, returns information about his/her TODO
import json
import urllib.request
from sys import argv


if __name__ == "__main__":
    # Getting the employee id from the argument
    employee_id = argv[1]

    # Constructing URLs
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'{url}/todos'

    # Employee names
    employee_name = json.loads(urllib.request.urlopen(
        url).read().decode("utf-8"))['name']

    # Todos
    todos = json.loads(urllib.request.urlopen(
        todos_url).read().decode("utf-8"))

    # Counting the completed tasks
    completed = sum(1 for i in todos if i['completed'])

    # Priting the output
    print("Employee {} is done with tasks({}/{}):"
          .format(employee_name, completed, len(todos)))
    [print(f"\t{todo['title']}") for todo in todos if todo['completed']]
