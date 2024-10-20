class Task:
    num_of_tasks = 0

    def __init__(self, id, note, status):
        self.id = id
        self.note = note
        self.status = status

        Task.num_of_tasks += 1
    #output without __str__
    # <__main__.Task object at 0x100ed39e0> Task removed successfully.
    def __str__(self):
        return f"{self.id} - ({self.status}) - {self.note}"

class myList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_id):
        """Add task to the list."""
        self.tasks.append(task_id)
        print("Task added successfully.")

    def remove_task(self, task_id):
        task_id = int(task_id)
        for x in self.tasks:
            if x.id == task_id:
                self.tasks.remove(x)
                print("Successfully removed: ", x)
                break
            else:
                print("Task not found.")

    def view_tasks(self, status=None):
        """View all tasks in the list."""
        if status == None:
            for x in self.tasks:
                print(f"{x.id} - ({x.status}) - {x.note}")
        elif status == "open":
            for x in self.tasks:
                if x.status == "open":
                    print(f"{x.id} - ({x.status}) - {x.note}")
        elif status == "done":
            for x in self.tasks:
                if x.status == "done":
                    print(f"{x.id} - ({x.status}) - {x.note}")


    def change_task(self, task_id):
        """Change task from the list."""

        for x in self.tasks:
            if x.id == task_id:
                print("current: ", x)
                x.note = input("Enter note: ")
                x.status = input("Enter status: ")
                print("Successfully changed: ", x)
                print("new: ", x)
                break
            else:
                print("Task not found.")

    def set_task_done(self, task_id):
        """Set task to DONE."""
        for x in self.tasks:
            if x.id == task_id:
                x.status = "done"
                print("Task set to DONE: ", x)
                break
            else:
                print("Task not found.")

    def save_to_file(self):
        pass
    def load_from_file(self):
        pass

def main():
    todo_list = myList()
    #initialize with some tasks
    todo_list.add_task(Task(Task.num_of_tasks, "Task 1", "open"))
    todo_list.add_task(Task(Task.num_of_tasks, "Task 2", "done"))
    todo_list.add_task(Task(Task.num_of_tasks, "Task 3", "open"))
    todo_list.add_task(Task(Task.num_of_tasks, "Task 4", "done"))

    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Change Task")
        print("5. Set Task to DONE")
        print("6. Show open Tasks")
        print("7. Save to file")
        print("8. Load from file")
        print("0. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            note = input("Enter note: ")
            #status = input("Enter status: ")
            todo_list.add_task(Task(Task.num_of_tasks, note, "open"))
        elif choice == "2":
            task_id = input("Enter task to be removed: ")
            todo_list.remove_task(int(task_id))
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            task_id = input("Enter task to be changed: ")
            todo_list.change_task(int(task_id))
        elif choice == "5":
            task_id = input("Enter task to be set to DONE: ")
            todo_list.set_task_done(int(task_id))
        elif choice == "6":
            todo_list.view_tasks("open")
        elif choice == "7":
            todo_list.save_to_file()
        elif choice == "8":
            todo_list.load_from_file()
        elif choice == "0":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()