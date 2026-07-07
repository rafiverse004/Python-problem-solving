# Check whether a number is a palindrome.

# Get a number from the user.
number = int(input("Enter a number: "))

# Store the original number.
original_number = number

# Reverse the number.
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

# Compare original and reversed numbers.
if original_number == reverse:
    print(f"{original_number} is a palindrome.")
else:
    print(f"{original_number} is not a palindrome.")