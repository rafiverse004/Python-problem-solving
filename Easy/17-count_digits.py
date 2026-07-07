# Count the number of digits in a given number.

# Get a number from the user.
number = int(input("Enter a number: "))

# Count digits.
count = 0

while number > 0:
    number //= 10
    count += 1

# Display the result.
print(f"Number of digits: {count}")