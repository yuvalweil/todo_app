# main.py

tasks = []  # Store tasks in memory

def show_menu():
    print("\n=== Personal Task Manager ===")
    print("1. Show tasks")
    print("2. Add a task")
    print("3. Delete a task")
    print("4. Exit")

def show_tasks():
    if not tasks:
        print("There are no tasks yet 🙂")
        return

    print("\nYour tasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def add_task():
    desc = input("Task description: ").strip()
    if desc:
        tasks.append(desc)
        print("✔ Task added!")
    else:
        print("❗ No task entered.")

def delete_task():
    show_tasks()
    if not tasks:
        return

    try:
        index = int(input("Task number to delete: "))
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"🗑 Task '{removed}' deleted.")
        else:
            print("❗ Invalid task number.")
    except ValueError:
        print("❗ Please enter a valid number.")

def main():
    while True:
        show_menu()
        choice = input("Choose an option (1-4): ").strip()

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("❗ Invalid choice, try again.")

if __name__ == "__main__":
    main()