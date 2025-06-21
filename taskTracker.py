#!/usr/bin/env python3

import os
import json
import sys
from datetime import datetime


TASK_FILE = './tasks.json'

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
    # This looks for the task with the current highest id and adds 1 to the id, so the next task gets assigned the new highest id.
    return max(task['id'] for task in tasks) + 1


def add_task(title):
    tasks = load_tasks()
    now = datetime.now()
    task = {
        'id': generate_id(tasks),
        'description': title,
        'status': 'todo',
        'createdAt': now.strftime('%Y-%m-%d %H:%M'),
        'updatedAt': now.strftime('%Y-%m-%d %H:%M')
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: [{task["id"]}] {task["description"]}")


def list_tasks(tasks):
    if not tasks:
        print("No task found, try adding some tasks using the \n\t add <task_description>")
        return
    for task in tasks:
         print(f'{task["id"]}.  {task["description"]} ({task["status"]})')
         print(f'\tCreated: {task["createdAt"]}, Updated: {task["updatedAt"]}')

def delete_tasks(task_id):
    tasks = load_tasks()
    new_tasks = [task for task in tasks if task_id != task["id"]]
    if len(new_tasks) == len(tasks):
        print(f"Task {task_id} not found.")
        return
    save_tasks(new_tasks)
    print(f"Task {task_id} has been deleted successfully.")


def print_usage():
    print('Usage:')
    print("\t python3 taskTracker.py Add <Task description>")


def main():
    if len(sys.argv) < 2:
        print_usage()
        return
    
    commands = ['Add', 'Delete', 'List']
    command = sys.argv[1]
    if command in commands:
        if command == "Add":
            if len(sys.argv) < 3:
                print("Please provide a task description")
            else:
                title = ' '.join(sys.argv[2:])
                add_task(title)
        elif command == "List":
            tasks = load_tasks()
            list_tasks(tasks)
        elif command == "Delete":
            if len(sys.argv) < 3 or not sys.argv[2].isdigit():
                print("Please provide the id of the task to be deleted :)")
            else:
                delete_tasks(int(sys.argv[2]))
    else:
        print("Unknown command: see usages")
        print_usage()
    

if __name__ == "__main__":
    main()
