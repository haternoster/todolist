if __name__ == "__main__":

    notes = []


    while True:
        print("> ", end = "")
        command = input()
        if command == "q":
            break
        if command == "list":
            for i in range(0, len(notes)):
                print(f"{i+1}. {notes[i]}")
            continue
        if command == "remove":
            print("removed")
            continue
        if command == "add":
            note = input()
            notes += [note]
            print("added")
            continue
        if command == "remove_last":
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


