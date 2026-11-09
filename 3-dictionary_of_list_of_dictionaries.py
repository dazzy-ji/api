#!/usr/bin/python3
"""
A Python script that exports the TODO list progress of all employees
into a single JSON file named todo_all_employees.json.
"""

import json
import requests


if __name__ == "__main__":
    base_url = "https://jsonplaceholder.typicode.com"

    users_res = requests.get("{}/users".format(base_url))
    todos_res = requests.get("{}/todos".format(base_url))

    if users_res.status_code == 200 and todos_res.status_code == 200:
        users = users_res.json()
        todos = todos_res.json()

        all_tasks = {}
        for user in users:
            user_id = str(user.get("id"))
            username = user.get("username")
            all_tasks[user_id] = []

            for task in todos:
                if task.get("userId") == user.get("id"):
                    task_dict = {
                        "username": username,
                        "task": task.get("title"),
                        "completed": task.get("completed"),
                    }
                    all_tasks[user_id].append(task_dict)

        filename = "todo_all_employees.json"
        with open(filename, mode="w", encoding="utf-8") as jsonfile:
            json.dump(all_tasks, jsonfile)
