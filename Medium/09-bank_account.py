# Create a simple bank account system.

# Store account details.
account_holder = input("Enter account holder name: ")
balance = 0

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Choose an option: ")

    # Deposit money.
    if choice == "1":
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Deposit successful.")

    # Withdraw money.
    elif choice == "2":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")

    # Display balance.
    elif choice == "3":
        print(f"{account_holder}'s balance: {balance}")

    # Exit system.
    elif choice == "4":
        break

    else:
        print("Invalid option.")