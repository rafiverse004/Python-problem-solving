# Calculate basic statistics from a list of numbers.

# Get numbers from the user.
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Calculate statistics.
total = sum(numbers)
average = total / len(numbers)
maximum = max(numbers)
minimum = min(numbers)

# Display results.
print(f"Sum: {total}")
print(f"Average: {average}")
print(f"Maximum: {maximum}")
print(f"Minimum: {minimum}")