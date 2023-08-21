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
    user_id = argv[1]
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
if __name__ == "__main__":
    """only execute the code when is main"""
    with open(f"{user_id}.json", mode='w') as f:

        dicted_json = {}
        listed_values = []
        for task in dicted_todos:
            aux_dict = {}
            aux_dict["task"] = f"{task.get('title')}"
            aux_dict["completed"] = f"{task.get('completed')}"
            aux_dict["username"] = f"{dicted_user.get('username')}"
            listed_values.append(aux_dict)
        dicted_json[f'{user_id}'] = listed_values
        json.dump(dicted_json, f)
        print(dicted_json)
