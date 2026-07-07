# Find the sum of all elements in a list.

# Get numbers from the user.
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Calculate the sum.
total = 0

for number in numbers:
    total += number

# Display the result.
print(f"Sum of elements: {total}")