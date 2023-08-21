#!/usr/bin/python3
"""
Employee TODO List Progress Script

This script fetches and displays information about
an employee's TODO list progress using a REST API.
It retrieves the user's TODO list based on the provided employee ID,
counts completed tasks,
and displays them along with the employee's name.
"""
import csv
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
    completed_tasks.append(x)
if __name__ == "__main__":
    """only execute the code when is main"""
    with open(f"{user_id}.csv", mode="w", newline='') as f:
        writted = csv.writer(f)
        for x in dicted_todos:
            f.write(f'"{user_id}","{dicted_user.get("name")}","{x.get("completed")}","{x.get("title")}"')
            f.write('\n')
