import datetime
import sys
def add_note():
    note = input("Write your note: ")
    now = datetime.datetime.now()
    with open("notes.txt", "a") as f:
        f.write(f"{now}: {note}\n")
    print("Note saved!")
def show_notes():
    try:
        with open("notes.txt", "r") as f: 
            print(f.read())
    except FileNotFoundError:
        print("No notes yet.")
running = True        
while running:
    print("\n1. add note 2. show notes 3. Exit")
    choice = input("Choose: ")
    if choice == "1":
        add_note()
    elif choice == "2":
        show_notes()
    elif choice == "3":
        print("Goodbye!")
        sys.exit()
                                      