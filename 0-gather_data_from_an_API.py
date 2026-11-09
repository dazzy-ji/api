#!/usr/bin/python3
"""
A Python script that fetches and displays an employee's TODO list progress
from a REST API based on their employee ID.
"""

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

            emp_name = user_data.get("name")
            total_tasks = len(todos_data)
            completed_tasks = [
                task for task in todos_data if task.get("completed") is True
            ]
            num_done = len(completed_tasks)

            print(
                "Employee {} is done with tasks({}/{}):".format(
                    emp_name, num_done, total_tasks
                )
            )
            for task in completed_tasks:
                print("\t {}".format(task.get("title")))
