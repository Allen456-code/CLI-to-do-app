FILENAME = "tasks.txt"

def show_menu():
    print("\n--- To-Do List ---")
    print("1. View tasks")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

def read_tasks():
    tasks = []
    try:
        file = open(FILENAME, "r")
        for line in file:
            tasks.append(line.strip())
        file.close()
    except FileNotFoundError:
        pass
    return tasks

def write_tasks(tasks):
    file = open(FILENAME, "w")
    for task in tasks:
        file.write(task + "\n")
    file.close()

def view_tasks():
    tasks = read_tasks()
    if not tasks:
        print("No tasks available.")
    else:
        print("Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter a task: ").strip()
    if task:
        tasks = read_tasks()
        tasks.append(task)
        write_tasks(tasks)
        print("Task added.")
    else:
        print("Empty task cannot be added.")

def remove_task():
    tasks = read_tasks()
    view_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to remove: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num - 1)
            write_tasks(tasks)
            print(f"Removed: {removed}")
        else:
            print("Invalid number.")
    except:
        print("Enter a valid number.")

while True:
    show_menu()
    choice = input("Choose (1-4): ").strip()
    if choice == "1":
        view_tasks()
    elif choice == "2":
        add_task()
    elif choice == "3":
        remove_task()
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Enter 1 to 4.")
        

        
        
