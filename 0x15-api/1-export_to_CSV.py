#!/usr/bin/python3
"""A script that using a employee ID, returns information about his/her TODO"""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    # Getting the employee id from the argument
    employee_id = argv[1]

    # Constructing URLs
    url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
    todos_url = f'{url}/todos'

    file_name = f"{employee_id}.csv"
    # Employee name
    username = requests.get(url).json()['username']
    todos = requests.get(todos_url).json()

    with open(file_name, 'w', newline='') as file_name:
        csvwriter = csv.writer(file_name, quoting=csv.QUOTE_ALL)
        for i in todos:
            csvwriter.writerow(
                [employee_id, username, i['completed'], i['title']])
