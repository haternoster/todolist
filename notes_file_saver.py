import csv
import os.path


class NotesSaver:
    def __init__(self, filename):
        self.filename = filename

    def is_file_exists(self):
        return os.path.isfile(self.filename)

    def load_from_file(self):
        if not self.is_file_exists():
            return []
        with open(self.filename, newline='') as csvfile:
            notesreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
            notes = []
            for note in notesreader:
                notes += [note[0]]
        return notes

    def save_to_file(self, notes_to_save):
        with open(self.filename, 'w', newline='') as csvfile:
            noteswriter = csv.writer(csvfile, delimiter=' ',
                                     quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for i in notes_to_save:
                noteswriter.writerow([i])
