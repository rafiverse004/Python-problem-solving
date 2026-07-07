# Find the maximum value in a list.

# Get numbers from the user.
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Assume the first number is the maximum.
maximum = numbers[0]

# Compare each number.
for number in numbers:
    if number > maximum:
        maximum = number

# Display the result.
print(f"Maximum value: {maximum}")