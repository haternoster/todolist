if __name__ == "__main__":

    while True:
        command = input()
        if command == "q":
            break
        if command == "list":
            print("list")
            continue
        if command == "remove":
            print("removed")
            continue
        if command == "add":
            print("add")
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


