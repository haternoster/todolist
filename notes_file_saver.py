import csv
import os.path


def is_file_exists(filename):
    return os.path.isfile(filename)


def load_from_file(filename):
    if not is_file_exists(filename):
        return []
    with open(filename, newline='') as csvfile:
        notesreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        notes = []
        for note in notesreader:
            notes += [note[0]]
    return notes


def save_to_file(filename, notes_to_save):
    with open(filename, 'w', newline='') as csvfile:
        noteswriter = csv.writer(csvfile, delimiter=' ',
                                 quotechar='|', quoting=csv.QUOTE_MINIMAL)
        for i in notes_to_save:
            noteswriter.writerow([i])
