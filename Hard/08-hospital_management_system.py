# Manage student records using classes.

class Student:
    # Store student information.
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    # Display student details.
    def display(self):
        print(
            f"Name: {self.name}, "
            f"Age: {self.age}, "
            f"Grade: {self.grade}"
        )


# Store students.
students = []

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Exit")

    choice = input("Choose an option: ")

    # Add student.
    if choice == "1":
        name = input("Enter name: ")
        age = input("Enter age: ")
        grade = input("Enter grade: ")

        student = Student(name, age, grade)
        students.append(student)

        print("Student added.")

    # Display students.
    elif choice == "2":
        for student in students:
            student.display()

    # Exit.
    elif choice == "3":
        break

    else:
        print("Invalid option.")