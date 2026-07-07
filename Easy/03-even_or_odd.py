# Check whether a number is even or odd.

# Get a number from the user.
number = int(input("Enter a number: "))

# Check the number type.
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")