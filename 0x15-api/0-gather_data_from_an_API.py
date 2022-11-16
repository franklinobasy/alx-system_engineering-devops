#!/usr/bin/python3
'''
Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.

Requirements:

1. You must use urllib or requests module
2. The script must accept an integer as a parameter, which is the employee ID
3. The script must display on the standard output the
   employee TODO list progress in this exact format:
    - First line: Employee EMPLOYEE_NAME is done with tasks
      (NUMBER_OF_DONE_TASKS/TOTAL_NUMBER_OF_TASKS):
        a. EMPLOYEE_NAME: name of the employee
        b. NUMBER_OF_DONE_TASKS: number of completed tasks
        c. TOTAL_NUMBER_OF_TASKS: total number of tasks,
           which is the sum of completed and non-completed tasks
    - Second and N next lines display the title of completed tasks: TASK_TITLE
        (with 1 tabulation and 1 space before the TASK_TITLE)
'''

import requests
import sys


id = int(sys.argv[1])
users = requests.get("https://jsonplaceholder.typicode.com/users").json()
todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()

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
            print(f"\t{title}")
        break
