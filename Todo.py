tasks = []

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append({"name": task, "done": False})

    elif choice == "2":
        if not tasks:
            print("No tasks yet.")
        else:
            for i, t in enumerate(tasks):
                status = "✓" if t["done"] else "✗"
                print(f"{i + 1}. [{status}] {t['name']}")

    elif choice == "3":
        number = int(input("Enter task number to delete: ")) - 1
        if 0 <= number < len(tasks):
            tasks.pop(number)
            print("Task deleted.")
        else:
            print("Invalid task number.")

    elif choice == "4":
        number = int(input("Enter task number to mark as completed: ")) - 1
        if 0 <= number < len(tasks):
            tasks[number]["done"] = True
            print("Task marked as completed.")
        else:
            print("Invalid task number.")

    elif choice == "5":
        break

    else:
        print("Invalid choice.")
