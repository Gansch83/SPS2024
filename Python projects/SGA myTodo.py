class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add task to the list."""
        self.tasks.append(task)
        print("Task added successfully.")

    def remove_task(self, task):
        """Remove task from the list."""
        print(task)
        print(self.tasks)
        if task in self.tasks:
            self.tasks.remove(task)
            print("Task removed successfully.")
        else:
            print("Task not found in the list.")

    def view_tasks(self):
        """View all tasks in the list."""
        if self.tasks:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                for key, value in task.items():
                    print(index, key, ":", value)

        else:
            print("No tasks found.")


def main():
    todo_list = ToDoList()

    task = {"Task1" : "open"}
    todo_list.add_task(task)
    task = {"Task2": "done"}
    todo_list.add_task(task)

    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            note = input("Enter note: ")
            status = input("Enter status: ")
            task = {note : status}
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Enter task to be removed: ")
            todo_list.remove_task(task)
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()