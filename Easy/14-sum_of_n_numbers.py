# Calculate the sum of the first N natural numbers.

# Get the value of N from the user.
number = int(input("Enter a number: "))

# Calculate the sum.
total = 0

for i in range(1, number + 1):
    total += i

# Display the result.
print(f"Sum of first {number} numbers is {total}.")