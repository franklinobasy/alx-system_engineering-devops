#!/usr/bin/python3
'''
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
'''

import requests
import sys


if (__name__ == "__main__") and (len(sys.argv) > 1):
    id = int(sys.argv[1])
    url = "https://jsonplaceholder.typicode.com"
    users = requests.get(f"{url}/users").json()
    todos = requests.get(f"{url}/todos").json()

    n_todos = 0
    n_tasks_completed = 0
    tasks_completed_title = []

    for todo in todos:
        if todo["userId"] == id:
            n_todos += 1
            if (todo["completed"]):
                n_tasks_completed += 1
                tasks_completed_title.append(todo["title"])

    for user in users:
        if user["id"] == id:
            text1 = f"Employee {user['name']} is done "
            text2 = f"with tasks({n_tasks_completed}/{n_todos}):"
            print(text1 + text2)
            for title in tasks_completed_title:
                print(f"\t {title}")
            break
