# Print the multiplication table of a given number.

# Get a number from the user.
number = int(input("Enter a number: "))

# Print multiplication table.
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")