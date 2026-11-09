#!/usr/bin/python3
"""
A Python script that extends Task 0 to export an employee's TODO list
progress into a JSON file format named USER_ID.json.
"""

import json
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) > 1:
        emp_id = sys.argv[1]
        base_url = "https://jsonplaceholder.typicode.com"

        user_res = requests.get("{}/users/{}".format(base_url, emp_id))
        todos_res = requests.get("{}/todos?userId={}".format(base_url, emp_id))

        if user_res.status_code == 200 and todos_res.status_code == 200:
            user_data = user_res.json()
            todos_data = todos_res.json()

            user_id = str(user_data.get("id"))
            username = user_data.get("username")

            task_list = []
            for task in todos_data:
                task_dict = {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": username,
                }
                task_list.append(task_dict)

            json_data = {user_id: task_list}
            filename = "{}.json".format(user_id)
            with open(filename, mode="w", encoding="utf-8") as jsonfile:
                json.dump(json_data, jsonfile)
