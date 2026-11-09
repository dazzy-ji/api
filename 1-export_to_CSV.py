#!/usr/bin/python3
"""
A Python script that extends Task 0 to export an employee's TODO list
progress into a CSV file format named USER_ID.csv.
"""

import csv
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

            filename = "{}.csv".format(user_id)
            with open(filename, mode="w", newline="") as csvfile:
                writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
                for task in todos_data:
                    completed = str(task.get("completed"))
                    title = task.get("title")
                    writer.writerow([user_id, username, completed, title])
