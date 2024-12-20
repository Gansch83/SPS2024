from myTodo_bib import MyList, Note


def main():
    todo_list = MyList()
    # docstring von load_from_file / "Magic Function" __doc__
    print(MyList.load_from_file.__doc__)

    todo_list.load_from_file("myTodo.csv")
    # initialize with some tasks
    # todo_list.add_task(Task(Task.num_of_notes, "Task 1", "open"))
    # todo_list.add_task(Task(Task.num_of_notes, "Task 2", "done"))
    # todo_list.add_task(Task(Task.num_of_notes, "Task 3", "open"))
    # todo_list.add_task(Task(Task.num_of_notes, "Task 4", "done"))

    while True:
        try:
            print("\nMy Notes & To-Do List")
            print("************************")
            print("Number of items: ", Note.num_of_notes)
            print("\n1. Add Note")
            print("2. Remove Note")
            print("3. View Notes")
            print("4. Change Note")
            print("5. Set Note to DONE")
            print("6. Show open Notes")
            print("7. Save to file")
            # print("8. Load from file")
            print("0. Quit")
            choice = input("Enter your choice: ")

            if choice == "1":
                note_desc = input("Enter description: ")
                todo_list.add_item(Note(Note.num_of_notes, "open", note_desc))
            elif choice == "2":
                todo_list.view_item()
                item_id = input("Enter item to be removed: ")
                todo_list.remove_item(int(item_id))
            elif choice == "3":
                todo_list.view_item()
            elif choice == "4":
                todo_list.view_item()
                item_id = input("Enter item to be changed: ")
                todo_list.change_item(int(item_id))
            elif choice == "5":
                todo_list.view_item()
                item_id = input("Enter item to be set to DONE: ")
                todo_list.set_item_done(int(item_id))
            elif choice == "6":
                todo_list.view_item("open")
            elif choice == "7":
                # not yet activated!!!
                # my_file = MyList.file_selection()
                todo_list.save_to_file("myTodo.csv")
            elif choice == "8":
                # not yet activated!!!
                my_file = MyList.file_selection()
                todo_list.load_from_file(my_file)
            elif choice == "0":
                if MyList.closing_app():
                    # save to file before quitting
                    todo_list.save_to_file("myTodo.csv")
                    MyList.static_smiley_code()
                    break
                else:
                    MyList.static_smiley_code()
                    break
            else:
                raise ValueError()
            # raise ValueError("ValueError txt: Invalid input. Please try again.")
            # Text vom except wird ausgegeben, wenn ValueError auftritt
        except ValueError:
            print("Invalid input. Please try again.")
        except Exception as e:
            print("Error: ", e)


if __name__ == "__main__":
    main()
