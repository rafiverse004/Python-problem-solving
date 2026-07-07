# Create a simple student database system.

# Store student records.
students = {}

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Choose an option: ")

    # Add a student.
    if choice == "1":
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        grade = input("Enter student grade: ")

        students[name] = {
            "age": age,
            "grade": grade
        }

        print("Student added.")

    # Display all students.
    elif choice == "2":
        for name, details in students.items():
            print(f"{name}: {details}")

    # Search for a student.
    elif choice == "3":
        name = input("Enter student name: ")

        if name in students:
            print(students[name])
        else:
            print("Student not found.")

    # Exit database.
    elif choice == "4":
        break

    else:
        print("Invalid option.")