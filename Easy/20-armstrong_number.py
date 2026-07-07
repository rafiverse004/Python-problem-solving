# Check whether a number is an Armstrong number.

# Get a number from the user.
number = int(input("Enter a number: "))

# Store the original number.
original_number = number

# Count the number of digits.
digits = len(str(number))

# Calculate Armstrong value.
sum_of_powers = 0

while number > 0:
    digit = number % 10
    sum_of_powers += digit ** digits
    number //= 10

# Compare the result.
if original_number == sum_of_powers:
    print(f"{original_number} is an Armstrong number.")
else:
    print(f"{original_number} is not an Armstrong number.")