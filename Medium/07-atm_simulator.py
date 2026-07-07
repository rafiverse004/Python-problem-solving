# Simulate basic ATM operations.

# Store account balance.
balance = 1000

while True:
    print("\n1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Choose an option: ")

    # Check balance.
    if choice == "1":
        print(f"Current balance: {balance}")

    # Deposit money.
    elif choice == "2":
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Money deposited.")

    # Withdraw money.
    elif choice == "3":
        amount = float(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance -= amount
            print("Please collect your money.")
        else:
            print("Insufficient balance.")

    # Exit ATM.
    elif choice == "4":
        break

    else:
        print("Invalid option.")