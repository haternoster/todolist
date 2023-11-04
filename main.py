from notes_file_saver import *

if __name__ == "__main__":

    notes = []
    notesfile = "notes.csv"

    notes = load_from_file(notesfile)
    while True:

        print("> ", end="")
        command = input()
        if command == "q":
            break
        if command == "list":
            for i in range(0, len(notes)):
                print(f"{i + 1}. {notes[i]}")
            if len(notes) == 0:
                print("list is empty")
            continue
        if command == "remove":
            index = int(input("index: "))
            new_notes = []
            for i in range(0, len(notes)):
                if index != (i + 1):
                    new_notes += [notes[i]]
            notes = new_notes
            save_to_file(notesfile, notes)
            print("removed")
            continue
        if command == "add":
            note = input("note: ")
            notes += [note]
            save_to_file(notesfile, notes)
            print("added")
            continue
        if command == "remove_last":
            del notes[-1]
            save_to_file(notesfile, notes)
            print("last removed")
            continue
        if command == "help":
            print("avaliable commands:")
            print("\t* q")
            print("\t* list")
            print("\t* remove")
            print("\t* add")
            print("\t* remove_last")
            print("\t* help")
            continue

        print(f"invalid command {command}")
