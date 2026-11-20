import json
import os

filename = "telefonbog.json"

def load_contacts():
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_contacts():
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(contacts, f, ensure_ascii=False, indent=4)

contacts = load_contacts()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def wait_for_back():
    print()
    while input ("press 0 to go back to the menu") != "0":
        pass

def get_contact():
    name = input("Enter contact name: ")
    phone_no = input("Enter contact phone number: ")
    return name, phone_no

def validate_phone(phone):
    phone = phone.replace(" ", "")
    if len(phone) == 8 and phone.isascii() and phone.isdigit():
        return phone
    return None


def add_contact(name, phone_no):
    phone_no = validate_phone(phone_no)
    if phone_no is None:
        print("Invalid number: it must be exactly 8 digits (spaces are okay).")
        return
    contacts[name] = phone_no
    save_contacts()
    print(f"Contact {name} added successfully.")

def search_contact(name):
    if name in contacts:
        print(f"Contact found: {name} - {contacts[name]}")
    else:
        print("Contact not found.")

def show_all_contacts():
    if contacts:
        print("All contacts:")
        for name, phone_no in contacts.items():
            print(f"{name}: {phone_no}")
    else:
        print("No contacts available.")

def goodbye():
    print("Goodbye! Thank you for using the contact manager.")

def exit():
    import sys
    sys.exit()


while True:
    print("1. Add contact")
    print("2. Search contact")
    print("3. Show all contacts")
    print("4. Exit")
    choice = input("Choose an option: ")

    clear_screen()  # Clear the screen before processing the choice

    if choice == "1":
        # indtast kontakt
        name, phone_no = get_contact()
        # tilføj kontakt med funktion
        add_contact(name, phone_no)  # Wait for user to go back to the menu

    elif choice == "2":
        # søg efter kontakt
        name = input("Enter the name to search: ")
        search_contact(name)# Wait for user to go back to the menu
    
    elif choice == "3":
        # vis alle kontakter
        loaded_contacts = load_contacts()  # Load contacts from the file
        contacts.update(loaded_contacts)  # Update the in-memory contacts with loaded contacts
        show_all_contacts()  # Wait for user to go back to the menu

    elif choice == "4":
        goodbye()  # Kald din luk-ned-funktion
        exit()

    else:
        print("Invalid option, please try again.")

    wait_for_back()  # Wait for user to go back to the menu