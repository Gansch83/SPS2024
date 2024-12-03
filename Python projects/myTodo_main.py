import myTodo_bib as bib

def main():
    todo_list = bib.MyList()
    todo_list.load_from_file()
    #initialize with some tasks
    #todo_list.add_task(Task(Task.num_of_tasks, "Task 1", "open"))
    #todo_list.add_task(Task(Task.num_of_tasks, "Task 2", "done"))
    #todo_list.add_task(Task(Task.num_of_tasks, "Task 3", "open"))
    #todo_list.add_task(Task(Task.num_of_tasks, "Task 4", "done"))

    while True:
        print("\n1. Add Task")
        print("2. Remove Task")
        print("3. View Tasks")
        print("4. Change Task")
        print("5. Set Task to DONE")
        print("6. Show open Tasks")
        print("7. Save to file")
        #print("8. Load from file")
        print("0. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            try:
                note = input("Enter note: ")
                #status = input("Enter status: ")
                todo_list.add_task(bib.Task(bib.Task.num_of_tasks, "open", note))
                print("Task added successfully.")
            except ValueError:
                print("Invalid input. Please try again.")
        elif choice == "2":
            try:
                task_id = input("Enter task to be removed: ")
                todo_list.remove_task(int(task_id))
            except ValueError:
                print("Invalid task id. Please try again.")
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            try:
                task_id = input("Enter task to be changed: ")
                todo_list.change_task(int(task_id))
            except ValueError:
                print("Invalid task id. Please try again.")
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