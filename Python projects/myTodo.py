myList = []
myList.append({"Staubsaugen" : "open"})
myList.append({"Fenster putzen" : "done"})
myList.append({"Schrank zusammenbauen" : "open"})
myList.append({"Python lernen" : "open"})

print(myList[1].items())
print(myList[1].keys())
print(myList[1].values())

def myPrint(list, key = "all"):
    print("You have {} notes:".format(len(list)))
    if key == "all":
        print("You have following ToDo´s on the list: ")
        for index, todo in enumerate(list, start = 1):
            print(index, todo)
            #print(list(todo.values())[index])
    elif key == "open":
        print("You have following open ToDo´s:")
        #for index, todo in enumerate(list, start = 1):
            #print(todo.items())
            #print(todo.keys())
            #print(todo.values())
            #if list(todo.values())[0] == 'open':
            #    print(index, todo)
            #else:
            #    pass

    elif key == "finished":
        print("You have following finished ToDo´s:")

    else:
        pass

while True:
    print("\nChoose from following options:")
    print("\na. Add Task")
    print("r. Remove Task")
    print("c. Change Task")
    print("p. Print Tasks")
    print("o. Print only open Tasks")
    print("f. Print only finished Tasks")
    print("s. Saving to file")
    print("l. Loading from file")
    print("q. Quit")
    select= input("Please select the option: ")

    if select == "a":
        entry = input("Enter task: ")
        myList.append({entry : "open"})

        print("added...")
    elif select == "r":
        myPrint(myList)
        entry = int(input("Enter # to be remove: ")) - 1
        # Bei Eingabe von 1 möchte man eigentlich den index 0 löschen
        # daher Eingabe minus 1
        popped = myList.pop(entry)

        print("ToDo {} has been removed!".format(popped))
    elif select == "c":
        myPrint(myList)
        entry = int(input("Enter # to be changed: ")) - 1
        # Bei Eingabe von 1 möchte man eigentlich den index 0 löschen
        # daher Eingabe minus 1
        entry1 = input("Enter updated ToDo: ")
        entry2 = input("Enter updated status: ")
        myList[entry] = {entry1 : entry2}

        print("updated...")
    elif select == "p":
        myPrint(myList)
    elif select == "o":
        myPrint(myList, "open")
    elif select == "f":
        myPrint(myList, "finished")
    elif select == "s":
        pass
    elif select == "l":
        pass
    elif select == "q":
        print("Thank you! \n Have a nice day! \n  :-) \n Exiting...")
        break
    else:
        print("Invalid selection. Please try again.")