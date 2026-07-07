# Find the second largest element in a list.

# Get numbers from the user.
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

# Remove duplicate values and sort the list.
unique_numbers = list(set(numbers))
unique_numbers.sort()

# Check if a second largest value exists.
if len(unique_numbers) >= 2:
    second_largest = unique_numbers[-2]
    print(f"Second largest element: {second_largest}")
else:
    print("Second largest element does not exist.")