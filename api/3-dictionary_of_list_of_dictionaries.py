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
all_users = requests.get("https://jsonplaceholder.typicode.com/users").json()
all_ids = (all_users[-1].get('id'))
for user in range(1, all_ids + 1):
    tasks_to_do = requests.get(f"https://jsonplaceholder.typicode.com/users/{user}/todos").json()
    user_data = requests.get(f"https://jsonplaceholder.typicode.com/users/{user}").json()
    dicted_json = {}
    listed_values = []
    for task in tasks_to_do:
        if task["userId"] == user:
            listed_values.append({
                "task": task.get('title'),
                "completed": task.get('completed'),
                "username": user_data.get('username')
            })
    dicted_json[user] = listed_values
    jsoned = json.dumps(dicted_json)
    with open("todo_all_employees.json", mode="w") as f:
        f.write(jsoned)
