#!/usr/bin/python3
"""A script that gathers data from an API"""
import json
import requests
from sys import argv
user_id = argv[1]
todos_requests = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}/todos")
user_request = requests.get(f"https://jsonplaceholder.typicode.com/users/{user_id}")
dicted_user = json.loads(user_request.text)
dicted_todos = json.loads(todos_requests.text)
completed_tasks = []
for x in dicted_todos:
    if x.get('completed') == True:
        completed_tasks.append(x.get('completed'))
print(f"Employee {dicted_user.get('name')} is done with tasks ({len(completed_tasks)}/{len(dicted_todos)})")
for task in dicted_todos:
    if task.get('completed') is True:
        print('\t ', end="")
        print(task.get('title'))
