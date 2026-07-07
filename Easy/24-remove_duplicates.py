# Remove duplicate values from a list.

# Get elements from the user.
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Store unique values.
unique_numbers = []

# Add only new values.
for number in numbers:
    if number not in unique_numbers:
        unique_numbers.append(number)

# Display the result.
print(f"List after removing duplicates: {unique_numbers}")