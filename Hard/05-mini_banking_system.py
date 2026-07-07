# Create a simple banking system using accounts.

# Store accounts.
accounts = {}


while True:
    print("\n1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    choice = input("Choose an option: ")

    # Create account.
    if choice == "1":
        name = input("Enter account name: ")
        accounts[name] = 0
        print("Account created.")

    # Deposit money.
    elif choice == "2":
        name = input("Enter account name: ")
        amount = float(input("Enter amount: "))

        accounts[name] += amount
        print("Deposit successful.")

    # Withdraw money.
    elif choice == "3":
        name = input("Enter account name: ")
        amount = float(input("Enter amount: "))

        if accounts[name] >= amount:
            accounts[name] -= amount
            print("Withdrawal successful.")
        else:
            print("Insufficient balance.")

    # Check balance.
    elif choice == "4":
        name = input("Enter account name: ")
        print(f"Balance: {accounts[name]}")

    # Exit.
    elif choice == "5":
        break

    else:
        print("Invalid option.")