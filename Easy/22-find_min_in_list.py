# Find the minimum value in a list.

# Get numbers from the user.
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Assume the first number is the minimum.
minimum = numbers[0]

# Compare each number.
for number in numbers:
    if number < minimum:
        minimum = number

# Display the result.
print(f"Minimum value: {minimum}")