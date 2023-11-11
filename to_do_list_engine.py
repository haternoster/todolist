from notes_file_saver import *


class ToDoList:
    def __init__(self, filename):
        self.filename = filename
        self.file_saver = NotesSaver(filename)
        self.notes = self.file_saver.load_from_file()

    def list_notes(self):
        for i in range(0, len(self.notes)):
            print(f"{i + 1}. {self.notes[i]}")
        if len(self.notes) == 0:
            print("list is empty")

    def remove(self):
        index = int(input("index: "))
        new_notes = []
        for i in range(0, len(self.notes)):
            if index != (i + 1):
                new_notes += [self.notes[i]]
        notes = new_notes
        self.file_saver.save_to_file(notes)
        print("removed")

    def add(self):
        note = input("note: ")
        self.notes += [note]
        self.file_saver.save_to_file(self.notes)
        print("added")

    def remove_last(self):
        del self.notes[-1]
        self.file_saver.save_to_file(self.notes)
        print("last removed")
