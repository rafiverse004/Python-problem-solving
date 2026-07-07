# Search contacts from a phonebook.

# Store phonebook contacts.
phonebook = {
    "Alice": "123456789",
    "Bob": "987654321",
    "Charlie": "555555555"
}

# Get search name.
name = input("Enter name to search: ")

# Search contact.
if name in phonebook:
    print(f"Phone number: {phonebook[name]}")
else:
    print("Contact not found.")