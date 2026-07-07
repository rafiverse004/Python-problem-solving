# Manage products and their quantities.

# Store inventory.
inventory = {}

while True:
    print("\n1. Add Product")
    print("2. View Inventory")
    print("3. Update Quantity")
    print("4. Exit")

    choice = input("Choose an option: ")

    # Add product.
    if choice == "1":
        name = input("Enter product name: ")
        quantity = int(input("Enter quantity: "))

        inventory[name] = quantity
        print("Product added.")

    # View inventory.
    elif choice == "2":
        for product, quantity in inventory.items():
            print(f"{product}: {quantity}")

    # Update product quantity.
    elif choice == "3":
        name = input("Enter product name: ")

        if name in inventory:
            quantity = int(input("Enter new quantity: "))
            inventory[name] = quantity
            print("Quantity updated.")
        else:
            print("Product not found.")

    # Exit manager.
    elif choice == "4":
        break

    else:
        print("Invalid option.")