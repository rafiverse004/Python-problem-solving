# Create a simple to-do list application.

# Store tasks.
tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    # Add a new task.
    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added.")

    # Display all tasks.
    elif choice == "2":
        if tasks:
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
        else:
            print("No tasks available.")

    # Remove a task.
    elif choice == "3":
        task_number = int(input("Enter task number to remove: "))

        if 1 <= task_number <= len(tasks):
            tasks.pop(task_number - 1)
            print("Task removed.")
        else:
            print("Invalid task number.")

    # Exit the program.
    elif choice == "4":
        break

    else:
        print("Invalid option.")