#!/usr/bin/env python3

import os
import json
import sys
from datetime import datetime


TASK_FILE = './tasks.json'
NOW = datetime.now()


def load_tasks():
    if not os.path.exists(TASK_FILE):
        return []
    with open(TASK_FILE, 'r') as taskList:
        try:
            return (json.load(taskList))
        except json.JSONDecodeError:
            return []


def save_tasks(tasks):
    with open(TASK_FILE, 'w') as taskList:
        try:
            json.dump(tasks, taskList, indent=4)
        except:
            print("Couldn't save task....")


def generate_id(tasks):
    if not tasks:
        return (1)
    # This looks for the task with the current highest id
    # and adds 1 to the id,
    # so the next task gets assigned the new highest id.
    return max(task['id'] for task in tasks) + 1


tasks = load_tasks()


def add_task(title):
    task = {
        'id': generate_id(tasks),
        'description': title,
        'status': 'todo',
        'createdAt': NOW.strftime('%Y-%m-%d %H:%M'),
        'updatedAt': NOW.strftime('%Y-%m-%d %H:%M')
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: [{task["id"]}] {task["description"]}")


def list_tasks():
    if not tasks:
        print("No task found, try \
              adding some tasks \
              using the \n\t add <task_description>")
        return
    for task in tasks:
        print(f'{task["id"]}.  {task["description"]} ({task["status"]})')
        print(f'\tCreated: {task["createdAt"]}, Updated: {task["updatedAt"]}')


def delete_tasks(task_id):
    new_tasks = [task for task in tasks if task_id != task["id"]]
    if len(new_tasks) == len(tasks):
        print(f"Task {task_id} not found.")
        return
    save_tasks(new_tasks)
    print(f"Task {task_id} has been deleted successfully.")


def mark_done(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'done'
            task['updatedAt'] = NOW.strftime('%Y-%m-%d %H:%M')
    save_tasks(tasks)
    print(f"Status for the task {task_id} set to DONE successfullly.")


def mark_inprogress(task_id):
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = 'inprogress'
            task['updatedAt'] = NOW.strftime('%Y-%m-%d %H:%M')
    save_tasks(tasks)
    print(f"Status for the task {task_id} set to INPROGRESS successfullly.")


def update(task_id, title):
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = title
            task['updatedAt'] = NOW.strftime('%Y-%m-%d %H:%M')
    save_tasks(tasks)
    print(f"Successfully updated task {task_id}.")


def list_todo():
    for task in tasks:
        if task['status'] == 'todo':
            print(f"{task["id"]}.  {task["description"]} ({task["status"]})")
            print(f'\tCreated: {task["createdAt"]}, \
                  Updated: {task["updatedAt"]}')


def list_inprogress():
    for task in tasks:
        if task['status'] == 'inprogress':
            print(f'{task["id"]}.  {task["description"]} ({task["status"]})')
            print(f'\tCreated: {task["createdAt"]}, \
                  Updated: {task["updatedAt"]}')


def list_done():
    for task in tasks:
        if task['status'] == 'done':
            print(f'{task["id"]}.  {task["description"]} ({task["status"]})')
            print(f'\tCreated: {task["createdAt"]}, Updated: \
                  {task["updatedAt"]}')


def print_usage():
    print('Usage:')
    print("\t python3 taskTracker.py Add <Task description>")
    print("\t python3 taskTracker.py List")
    print("\t python3 taskTracker.py Delete <task_id>")
    print("\t python3 taskTracker.py Mark-in-progress <task_id>")
    print("\t python3 taskTracker.py Mark-done <task_id>")
    print("\t python3 taskTracker.py Update <task_id> <description>")
    print()


def main():
    if len(sys.argv) < 2:
        print_usage()
        return

    commands = ['Add', 'Delete',
                'List', 'Mark-in-progress',
                'Mark-done', 'Update', "List-inprogress",
                "List-todo", "List-done"]
    command = sys.argv[1]
    if command in commands:
        if command == "Add":
            if len(sys.argv) < 3:
                print("Please provide a task description")
            else:
                title = ' '.join(sys.argv[2:])
                add_task(title)
        elif command == "List":
            list_tasks()
        elif command == "Delete":
            if len(sys.argv) < 3 or not sys.argv[2].isdigit():
                print_usage()
            else:
                delete_tasks(int(sys.argv[2]))
        elif command == "Mark-done":
            if len(sys.argv) < 3 or not sys.argv[2].isdigit():
                print_usage()
            else:
                mark_done(int(sys.argv[2]))
        elif command == "Mark-in-progress":
            if len(sys.argv) < 3 or not sys.argv[2].isdigit():
                print_usage()
            else:
                mark_inprogress(int(sys.argv[2]))
        elif command == "Update":
            if len(sys.argv) < 4 or not sys.argv[2].isdigit():
                print_usage()
            else:
                update(int(sys.argv[2]), sys.argv[3])
        elif command == "List-todo":
            list_todo()
        elif command == "List-inprogress":
            list_inprogress()
        elif command == "List-done":
            list_done()

    else:
        print("Unknown command: see usages")
        print_usage()


if __name__ == "__main__":
    main()
