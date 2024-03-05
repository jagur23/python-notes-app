import random
from data_create import*

import json
import os
import datetime


def create_note():
    notes = load_notes()
    new_note = {}
    id = random.randint(1, 1000000)
    new_note["id"] = id
    new_note["title"] = title_input()
    new_note["body"] = body_input()
    new_note["date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    notes.append(new_note)
    write_note(notes)
    print("The note is successfully added!")
    print()


def load_notes():
    if os.path.exists("notes.json"):
        with open("notes.json", "r") as file:
            notes = json.load(file)
        return notes
    else:
        return []
    

def write_note(notes):
    with open("notes.json", "w") as file:
        json.dump(notes, file, indent=4)


def print_all_notes():
    print("Your notes list: ")
    print()
    notes = load_notes()
    for note in notes:
        print(f"{note['date']} - id {note['id']} / {note['title']}")
    print()


def edit_note():
    print_all_notes()
    notes = load_notes()
    try:
        note_id = int(input("Enter note ID for editing: "))
        for note in notes:
            if note["id"] == note_id:
                note["title"] = input("Write new title: ")
                note["body"] = input("Write new note body: ")
                note["date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                write_note(notes)
                print("Editing was successful!")
                print()
                return
        print("Note with this ID was not found! Try again.")
        print()
    except ValueError:
        print("Wrong input! ID is a number.")
        print()


def delete_note():
    print_all_notes()
    notes = load_notes()
    try:
        note_id = int(input("Enter the note ID to delete: "))
        for note in notes:
            if note["id"] == note_id:
                notes = [note for note in notes if note["id"] != note_id]
                write_note(notes)
                print("Note deleted successfully!")
                print()
                return
        print("Note with this ID was not found! Try again.")
        print()
    except ValueError:
        print("Wrong input! ID is a number.")
        print()


def read_note_by_id():
    print_all_notes()
    notes = load_notes()
    try:
        note_id = int(input("Enter the ID of the note you want to read: "))
        print()
        for note in notes:
            if note["id"] == note_id:
                print(f"Note ID {note['id']} / {note['title']} : {note['body']}.")
                print()
                return
        print("Wrong note ID! Try again.")
    except ValueError:
            print("Wrong input! ID is a number.")
            print()


def search_notes_by_date():
    return