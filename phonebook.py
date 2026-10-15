import json
def save_contacts(contacts):
    with open("contacts.json", "w") as f:
         json.dump(contacts, f) 
def load_contacts():
    try:
        with open("contacts.json", "r") as f:
             return json.loads(f)
    except FileNotFoundError: 
        return []
def add_contact(contacts):
    name = input("name: ") 
    phone = input("phone: ")
    contacts.append({"name": name, "phone": phone})
    save_contacts(contacts)
    print("contact added!")
def show_contacts(contacts):
     for contact in contacts:
         print(contact["name"], "_", contact["phone"]) 
contacts =load_contacts()
while True:         
    print("\n1. add  2. show  3. exit")
    choice = input("choose: ")
    if choice == "1":
        add_contact(contacts)
    elif choice == "2":
        show_contacts(contacts)
    elif choice == "3":
        break        
          
    