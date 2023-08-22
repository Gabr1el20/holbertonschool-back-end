#!/usr/bin/python3
"""A script that lists all tasks from all users"""
import json
import requests


def fetch_todo_list(user_id):
    """fetch the API data of todo's list"""
    tasks_to_do = requests.get(f"https://jsonplaceholder.typicode.com"
                               f"/users/{user_id}/todos").json()
    user_data = requests.get(f"https://jsonplaceholder"
                             f".typicode.com/users/{user_id}").json()

    listed_values = []
    for task in tasks_to_do:
        listed_values.append({
            "task": task.get('title'),
            "completed": task.get('completed'),
            "username": user_data.get('username')
        })

    return listed_values


def main():
    "Entry point"
    all_users = requests.get("https://jsonplaceholder"
                             f".typicode.com/users").json()
    all_ids = len(all_users)

    user_tasks = {}
    for user_id in range(1, all_ids + 1):
        user_tasks[user_id] = fetch_todo_list(user_id)

    with open("todo_all_employees.json", mode="w") as f:
        json.dump(user_tasks, f)


if __name__ == "__main__":
    main()
