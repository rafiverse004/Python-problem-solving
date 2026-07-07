# Track personal expenses and calculate total spending.

# Store expenses.
expenses = []

while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Show Total")
    print("4. Exit")

    choice = input("Choose an option: ")

    # Add expense.
    if choice == "1":
        name = input("Enter expense name: ")
        amount = float(input("Enter amount: "))

        expenses.append({"name": name, "amount": amount})
        print("Expense added.")

    # View expenses.
    elif choice == "2":
        for expense in expenses:
            print(f"{expense['name']}: {expense['amount']}")

    # Calculate total expense.
    elif choice == "3":
        total = 0

        for expense in expenses:
            total += expense["amount"]

        print(f"Total expense: {total}")

    # Exit tracker.
    elif choice == "4":
        break

    else:
        print("Invalid option.")