# Manage books in a simple library system.

# Store available books.
books = []

while True:
    print("\n1. Add Book")
    print("2. View Books")
    print("3. Borrow Book")
    print("4. Exit")

    choice = input("Choose an option: ")

    # Add a book.
    if choice == "1":
        book = input("Enter book name: ")
        books.append(book)
        print("Book added.")

    # Display books.
    elif choice == "2":
        if books:
            for book in books:
                print(book)
        else:
            print("No books available.")

    # Borrow a book.
    elif choice == "3":
        book = input("Enter book name: ")

        if book in books:
            books.remove(book)
            print("Book borrowed.")
        else:
            print("Book not available.")

    # Exit system.
    elif choice == "4":
        break

    else:
        print("Invalid option.")