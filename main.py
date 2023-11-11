from to_do_list_engine import *

if __name__ == "__main__":

    notesfile = "notes.csv"

    to_do_list_engine = ToDoList(notesfile)

    while True:

        print("> ", end="")
        command = input()
        if command == "quit" or command == "q":
            break
        if command == "switch":
            notesfile = input("switch to: ") + ".csv"
            to_do_list_engine = ToDoList(notesfile)
            continue
        if command == "list":
            to_do_list_engine.list_notes()
            continue
        if command == "remove":
            to_do_list_engine.remove()
            continue
        if command == "add":
            to_do_list_engine.add()
            continue
        if command == "remove_last":
            to_do_list_engine.remove_last()
            continue
        if command == "help" or command == "h":
            print("available commands:")
            print("\t* q")
            print("\t* list")
            print("\t* remove")
            print("\t* add")
            print("\t* remove_last")
            print("\t* help")
            continue
        print(f"invalid command {command}")