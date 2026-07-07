# Print the Fibonacci series up to N terms.

# Get the number of terms.
terms = int(input("Enter the number of terms: "))

# Initialize first two Fibonacci numbers.
first_number = 0
second_number = 1

# Generate Fibonacci series.
for _ in range(terms):
    print(first_number, end=" ")

    next_number = first_number + second_number
    first_number = second_number
    second_number = next_number