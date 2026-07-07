# Create an address book that stores contacts in a file.

import json

# File to store contacts.
file_name = "contacts.json"


# Load contacts from file.
try:
    with open(file_name, "r") as file:
        contacts = json.load(file)
except FileNotFoundError:
    contacts = {}


while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Choose an option: ")

    # Add a contact.
    if choice == "1":
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        address = input("Enter address: ")

        contacts[name] = {
            "phone": phone,
            "address": address
        }

        with open(file_name, "w") as file:
            json.dump(contacts, file, indent=4)

        print("Contact saved.")

    # View contacts.
    elif choice == "2":
        for name, details in contacts.items():
            print(name, details)

    # Search contact.
    elif choice == "3":
        name = input("Enter name: ")

        if name in contacts:
            print(contacts[name])
        else:
            print("Contact not found.")

    # Exit.
    elif choice == "4":
        break

    else:
        print("Invalid option.")