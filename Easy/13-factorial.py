# Find the factorial of a given number.

# Get a number from the user.
number = int(input("Enter a number: "))

# Calculate factorial.
factorial = 1

for i in range(1, number + 1):
    factorial *= i

# Display the result.
print(f"Factorial of {number} is {factorial}.")