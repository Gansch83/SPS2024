import csv

class Task:
    num_of_tasks = 0

    def __init__(self, task_id, status, note):
        """Initialize task with task_id, status and note."""
        self.task_id = task_id
        self.status = status
        self.note = note

        Task.num_of_tasks += 1

    def __del__(self):
        """Destructor."""
        Task.num_of_tasks -= 1

    #output without __str__
    # <__main__.Task object at 0x100ed39e0> Task removed successfully.
    # In addition, writing the output format multiple times is not efficient. -> DRY -> DON'T REPEAT YOURSELF!!!
    def __str__(self):
        return f"{self.task_id} - ({self.status}) - {self.note}"

class MyList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Add task to the list."""
        self.tasks.append(task)
        #print("Task added successfully.")

    def remove_task(self, task_id):
        """Remove task from the list."""
        for todo in self.tasks:
            if todo.task_id == task_id:
                self.tasks.remove(todo)
                print("Successfully removed: ", todo)
                break
        else:
            print("Task not found.")

    def view_tasks(self, status=None):
        """View all tasks in the list."""
        if len(self.tasks) == 0:
            print("No tasks in the list.")
            return
        if status is None:
            for todo in self.tasks:
                print(todo)
        elif status == "open":
            for todo in self.tasks:
                if todo.status == "open":
                    print(todo)
        elif status == "done":
            for todo in self.tasks:
                if todo.status == "done":
                    print(todo)

    def change_task(self, task_id):
        """Change task from the list."""
        for todo in self.tasks:
            if todo.task_id == task_id:
                print("current: ", todo)
                todo.note = input("Enter note: ")
                todo.status = input("Enter status: ")
                print("updated: ", todo)
                break
        else:
            print("Task not found.")

    def set_task_done(self, task_id):
        """Set task to DONE."""
        for todo in self.tasks:
            if todo.task_id == task_id:
                todo.status = "done"
                print("Task set to DONE: ", todo)
                break
        else:
            print("Task not found.")

    def save_to_file(self):
        with open("myTodo.csv", "w") as csv_file:
            csv_writer = csv.DictWriter(csv_file, fieldnames=["task_id", "status", "note"], delimiter="\t")
            csv_writer.writeheader()

            for task in self.tasks:
                csv_writer.writerow({"task_id": task.task_id, "status": task.status, "note": task.note})

    def load_from_file(self):
        # working folder is the folder where the script is located
        with open("myTodo.csv", "r") as csv_file:
            csv_reader = csv.DictReader(csv_file, delimiter="\t")

            for line in csv_reader:
                #print(line)
                self.add_task(Task(int(line["task_id"]), line["status"], line["note"]))

        print(f"Successfully loaded from file {csv_file.name}.")
