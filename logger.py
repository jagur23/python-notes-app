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
    print('The note is successfully added!')
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
    return

def edit_note():   ## last modifying data and time
    return

def remove_note():
    return

def search_note():
    return