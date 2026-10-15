import json
def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []
def save_tasks(tasks):
     with open("task.json", "w") as f:
         json.dump(tasks, f)
def add_task(tasks):
     task =input("Enter task: ")
     tasks.append({"task": task, "done": False})
     save_tasks(tasks)
     print("Task added!")
def show_tasks(tasks):
     for i, task in enumerate(tasks):
         status = "x" if task["done"] else "[ ]"
         print(f"{i+1}. [{status}] {task['task']}")
tasks = load_tasks()
while True:
     print("\n1.  Add 2. Show  3. Exit")
     choice = input("Choose: ")
     if choice == "1":
         add_task(tasks)
     elif choice == "2":
         show_tasks(tasks)
     elif choice == "3":
         break
                                   