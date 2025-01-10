def display_menu():
    print("\nTo-Do List Manager")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Update a task")
    print("4. Remove a task")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("\nNo tasks in the to-do list.")
    else:
        print("\nTo-Do List:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['title']} - {'Completed' if task['completed'] else 'Pending'}")

def add_task(tasks):
    title = input("\nEnter task title: ").strip()
    if title:
        tasks.append({"title": title, "completed": False})
        print("Task added successfully.")
    else:
        print("Task title cannot be empty.")

def update_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter the task number to update: "))
            if 1 <= task_num <= len(tasks):
                new_title = input("Enter new task title (leave blank to keep current): ").strip()
                if new_title:
                    tasks[task_num - 1]["title"] = new_title
                status = input("Mark as completed? (yes/no): ").strip().lower()
                if status in ["yes", "y"]:
                    tasks[task_num - 1]["completed"] = True
                elif status in ["no", "n"]:
                    tasks[task_num - 1]["completed"] = False
                print("Task updated successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def remove_task(tasks):
    view_tasks(tasks)
    if tasks:
        try:
            task_num = int(input("\nEnter the task number to remove: "))
            if 1 <= task_num <= len(tasks):
                removed_task = tasks.pop(task_num - 1)
                print(f"Task '{removed_task['title']}' removed successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    tasks = []
    while True:
        display_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            update_task(tasks)
        elif choice == "4":
            remove_task(tasks)
        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
