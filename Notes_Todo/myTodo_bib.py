import csv

"""
File: myTodo_bib.py
Author: Bernarda, Dominik, Stefan
Date: 2024-12-07

This module contains the classes Note, Task and MyList.
Note is the parent class of Task.
MyList is a class that contains a list of Note and Task objects.
The class MyList has methods to add, remove, view, change and set items to done.
The class MyList also has methods to save and load the list to and from a csv file.
"""


class Note:
    num_of_notes = 0

    def __init__(self, note_id, status, desc):
        """Initialize task with note_id, status and note."""
        self.note_id = note_id
        self.status = status
        self.desc = desc

        Note.num_of_notes += 1

    def __del__(self):
        """Destructor."""
        Note.num_of_notes -= 1

    # output without __str__
    # <__main__.Task object at 0x100ed39e0> Task removed successfully.
    # In addition, writing the output format multiple times is not efficient. -> DRY -> DON'T REPEAT YOURSELF!!!
    def __str__(self):
        return f"{self.status} - {self.desc}"


class Task(Note):

    def __init__(self, note_id, status, desc, done_dat):
        """Initialize task with task_id, status, note and done_dat."""
        Note.__init__(self, note_id, status, desc)
        self.done_dat = done_dat

    def __str__(self):
        return f"{self.status} - {self.desc} - {self.done_dat}"


class MyList:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        """Add item to the list."""
        self.items.append(item)
        print("Item added successfully.")

    def remove_item(self, item_id):
        """Remove item from the list."""
        try:
            print("Item successfully removed: ", self.items.pop(item_id))
        except ValueError:
            print("Wrong Value.")
        except IndexError:
            print("Wrong Index.")
        except Exception as e:
            print("Error: ", e)

    def view_item(self, status=None):
        """View all items in the list."""
        print("=====START=====")
        if len(self.items) == 0:
            print("No items in the list.")
            return
        if status is None:
            # print all items with list index
            for item in self.items:
                print("#{}. {}".format(self.items.index(item), item))
        elif status == "open":
            for item in self.items:
                if item.status == "open":
                    print("#{}. {}".format(self.items.index(item), item))
        elif status == "done":
            for item in self.items:
                if item.status == "done":
                    print("#{}. {}".format(self.items.index(item), item))
        print("=====END=====")

    def change_item(self, item_id):
        """Change item from the list."""
        try:
            print("current: ", self.items[item_id])
            self.items[item_id].desc = input("Enter NEW description: ")
            self.items[item_id].status = input("Enter NEW status: ")
        except ValueError:
            print("Wrong Value.")
        except IndexError:
            print("Wrong Index.")
        except Exception as e:
            print("Error: ", e)
        else:
            # else is executed if no exception occurs
            print("Item changed successfully.", self.items[item_id])

    def set_item_done(self, item_id):
        """Set item to DONE."""
        try:
            self.items[item_id].status = "done"
        except ValueError:
            print("Wrong Value.")
        except IndexError:
            print("Wrong Index.")
        except Exception as e:
            print("Error: ", e)
        else:
            # else is executed if no exception occurs
            print("Item set to DONE: ", self.items[item_id])

    def save_to_file(self, para_file):
        # working folder is the folder where the script is located
        try:
            # open() sollte mit einem Kontextmanager (with) verwendet werden, um sicherzustellen,
            # dass die Datei automatisch geschlossen wird.
            with open(para_file, "w") as csv_file:
                csv_writer = csv.DictWriter(csv_file, fieldnames=["note_id", "status", "desc"], delimiter="\t")
                csv_writer.writeheader()
                for item in self.items:
                    csv_writer.writerow({"note_id": item.note_id, "status": item.status, "desc": item.desc})

            # csv_file = open("myTodo.csv", "w")
            # csv_writer = csv.DictWriter(csv_file, fieldnames=["note_id", "status", "desc"], delimiter="\t")
            # csv_writer.writeheader()
            # for item in self.items:
            #    csv_writer.writerow({"note_id": item.note_id, "status": item.status, "desc": item.desc})
        except FileExistsError:
            print("File already exists!")
        except Exception as e:
            print("Error: ", e)
        else:
            # else is executed if no exception occurs
            print("Successfully saved to file.")
        finally:
            # finally is executed no matter what
            # csv_file.close()
            print("file closed.")

    @staticmethod
    def file_selection():
        """Select file."""
        try:
            para_file = input("Enter file name to be used: ")
            return para_file
        except Exception as e:
            print("Error: ", e)

    def load_from_file(self, para_file):
        """LOADING csv-file: working folder is the folder where the script is located"""
        try:
            # open() sollte mit einem Kontextmanager (with) verwendet werden, um sicherzustellen,
            # dass die Datei automatisch geschlossen wird.
            with open(para_file, "r") as csv_file:
                csv_reader = csv.DictReader(csv_file, delimiter="\t")
                for line in csv_reader:
                    self.add_item(Note(int(line["note_id"]), line["status"], line["desc"]))

            # csv_file = open("myTodo.csv", "r")
            # csv_reader = csv.DictReader(csv_file, delimiter="\t")
            # for line in csv_reader:
            #    self.add_item(Note(int(line["note_id"]), line["status"], line["desc"]))
        except FileNotFoundError:
            print("File not found!")
        except Exception as e:
            print("Error: ", e)
        else:
            # else is executed if no exception occurs
            print(f"Successfully loaded from file {csv_file.name}.")
        finally:
            # finally is executed no matter what
            # csv_file.close()
            print("file closed.")

    @staticmethod
    def closing_app():
        """Closing the app."""
        try:
            print("Do you want to save before closing?")
            choice = input("Enter 'y' for yes or 'n' for no: ")
            if choice.upper() == "Y":
                return True
            elif choice.upper() == "N":
                return False
            else:
                raise ValueError()
        except ValueError:
            print("Invalid input. Please try again.")
        except Exception as e:
            print("Error: ", e)

    @staticmethod
    def static_smiley_code():
        """A static method is a method that belongs to a class rather than an instance of the class.
        It does not require access to the instance (self) or class (cls) variables"""
        try:
            print('''
                  , ; ,   .-'"""'-.   , ; ,
                  \\|/  .'         '.  \|//
                   \-;-/   ()   ()   \-;-/
                   // ;               ; \\
                  //__; :.         .; ;__\\
                 `-----\'.'-.....-'.'/-----'
                        '.'.-.-,_.'.'
                jgs       '(  (..-'
                            '-'    
            ''')
        except Exception as e:
            print("Error: ", e)
