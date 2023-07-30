import datetime


tasks_by_user = {}

users = {}

def register():
    username = input("Enter your desired username: ")
    if username in users:
        print("Username already exists. Please choose a different username.")
        return

    password = input("Enter your desired password: ")
    tasks_by_user[username] = []
    users[username] = password
    print("Registration successful. You can now log in.")

def login():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username] == password:
        print("Login successful!")
        return username
    else:
        print("Invalid username or password. Please try again.")
        return None

def add_task(username):
    title = input("Enter the task title: ")
    description = input("Enter the task description: ")
    due_date = input("Enter the task due date (YYYY-MM-DD): ")
    priority = input("Enter the task priority (High/Medium/Low): ")
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "priority": priority
    }
    tasks_by_user[username].append(task)
    print("Task added successfully!")

def update_task(username):
    task_name = input("Enter the name of the task you want to update: ")

    found_task = None
    for task in tasks_by_user[username]:
        if task['title'] == task_name:
            found_task = task
            break

    if found_task is None:
        print(f"Task with the name '{task_name}' not found.")
    else:
        print(f"Updating task: {found_task['title']}")
        print("Leave the field empty if you don't want to update it.")

        new_title = input("Enter new task title (leave empty to keep current title): ")
        new_description = input("Enter new task description (leave empty to keep current description): ")
        new_due_date = input("Enter new task due date (YYYY-MM-DD) (leave empty to keep current due date): ")
        new_priority = input("Enter new task priority (High/Medium/Low) (leave empty to keep current priority): ")

        if new_title:
            found_task['title'] = new_title
        if new_description:
            found_task['description'] = new_description
        if new_due_date:
            found_task['due_date'] = new_due_date
        if new_priority:
            found_task['priority'] = new_priority

        print("Task updated successfully!")

def delete_task(username):
    task_name = input("Enter the name of the task you want to delete: ")

    task_index = None
    for idx, task in enumerate(tasks_by_user[username]):
        if task['title'] == task_name:
            task_index = idx
            break

    if task_index is None:
        print(f"Task with the name '{task_name}' not found.")
    else:
        deleted_task = tasks_by_user[username].pop(task_index)
        print(f"Task '{deleted_task['title']}' has been deleted.")

def display_tasks(username):
    user_tasks = tasks_by_user[username]

    if not user_tasks:
        print("No tasks found for this user.")
    else:
        print("Tasks for", username)
        for idx, task in enumerate(user_tasks):
            print(f"{idx + 1}. {task['title']} - {task['due_date']} - {task['priority']}")

def set_task_reminder(username):
    current_date = datetime.date.today()

    user_tasks = tasks_by_user[username]

    if not user_tasks:
        print("No tasks found for this user.")
        return

    print("Tasks for", username)
    display_tasks(username)

    task_idx = int(input("Enter the task number to set a reminder for: ")) - 1
    if task_idx < 0 or task_idx >= len(user_tasks):
        print("Invalid task number. No reminder set.")
        return

    selected_task = user_tasks[task_idx]

    due_date = datetime.datetime.strptime(selected_task["due_date"], "%Y-%m-%d").date()
    if due_date >= current_date:
        print(f"Reminder: Task '{selected_task['title']}' is due on {selected_task['due_date']}.")
    else:
        print("The task due date has already passed. No reminder set.")


def main():
    logged_in_username = None

    while not logged_in_username:
        print("\n==== Daily Task Scheduler ====")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            register()
        elif choice == "2":
            logged_in_username = login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

    while logged_in_username:
        print("\n==== Daily Task Scheduler ====")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. View Tasks")
        print("5. Set Task Reminder")
        print("6. Logout")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_task(logged_in_username)
        elif choice == "2":
            update_task(logged_in_username)
        elif choice == "3":
            delete_task(logged_in_username)
        elif choice == "4":
            display_tasks(logged_in_username)
        elif choice == "5":
            set_task_reminder(logged_in_username)
        elif choice == "6":
            logged_in_username = None
            print("Logged out.")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
