#!/usr/bin/python3
"""
Employee TODO List Progress Script

This script fetches and displays information about
an employee's TODO list progress using a REST API.
It retrieves the user's TODO list based on the provided employee ID,
counts completed tasks,
and displays them along with the employee's name.
"""
import json
import requests
from sys import argv
user_id = None
try:
    user_id = argv[2]
except Exception as e:
    pass
todos_requests = requests.get(f"https://jsonplaceholder"
                              f".typicode.com/users/{user_id}/todos")
user_request = requests.get(f"https://jsonplaceholder"
                            f".typicode.com/users/{user_id}")
dicted_user = json.loads(user_request.text)
dicted_todos = json.loads(todos_requests.text)
completed_tasks = []
for x in dicted_todos:
    if x.get('completed') is True:
        completed_tasks.append(x.get('completed'))
print(f"Employee {dicted_user.get('name')}"
      f" is done with tasks ({len(completed_tasks)}/{len(dicted_todos)}):")
if __name__ == "__main__":
    """only execute the code when is main"""
    for task in dicted_todos:
        if task.get('completed') is True:
            print('\t ', end="")
            print(task.get('title'))
