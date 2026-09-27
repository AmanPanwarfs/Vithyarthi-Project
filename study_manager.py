from datetime import datetime
from modules.data_manager import load_tasks, save_tasks


def add_task():
    tasks = load_tasks()

    subject = input("Subject: ").strip()
    topic = input("Topic: ").strip()
    priority = input("Priority (High/Medium/Low): ").strip().title()

    if priority not in {"High", "Medium", "Low"}:
        priority = "Medium"

    task_id = max([task["id"] for task in tasks], default=0) + 1

    task = {
        "id": task_id,
        "subject": subject,
        "topic": topic,
        "priority": priority,
        "status": "Pending",
        "created": datetime.now().strftime("%Y-%m-%d")
    }

    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully.")


def view_tasks():
    tasks = load_tasks()

    if not tasks:
        print("No study tasks found.")
        return

    print("\n" + "-" * 78)
    print(f"{'ID':<5}{'Subject':<18}{'Topic':<25}{'Priority':<12}{'Status':<12}")
    print("-" * 78)

    for task in tasks:
        print(
            f"{task['id']:<5}{task['subject'][:17]:<18}"
            f"{task['topic'][:24]:<25}{task['priority']:<12}{task['status']:<12}"
        )


def complete_task():
    tasks = load_tasks()

    if not tasks:
        print("No tasks available.")
        return

    view_tasks()

    try:
        task_id = int(input("\nEnter task ID to mark completed: "))
    except ValueError:
        print("Please enter a valid numeric ID.")
        return

    found = False
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "Completed"
            found = True
            break

    if found:
        save_tasks(tasks)
        print("Task marked as completed.")
    else:
        print("Task ID not found.")


def delete_task():
    tasks = load_tasks()

    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("Please enter a valid numeric ID.")
        return

    updated = [task for task in tasks if task["id"] != task_id]

    if len(updated) == len(tasks):
        print("Task ID not found.")
    else:
        save_tasks(updated)
        print("Task deleted.")


def study_menu():
    while True:
        print("\n--- STUDY MANAGER ---")
        print("1. Add study task")
        print("2. View tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Back")

        choice = input("Choice: ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            complete_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")
