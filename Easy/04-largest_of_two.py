# Find the largest among two numbers.

# Get two numbers from the user.
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Compare the numbers.
if first_number > second_number:
    largest = first_number
elif second_number > first_number:
    largest = second_number
else:
    largest = None

# Display the result.
if largest is not None:
    print(f"Largest number is {largest}.")
else:
    print("Both numbers are equal.")