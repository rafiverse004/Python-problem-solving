# Reverse the digits of a number.

# Get a number from the user.
number = int(input("Enter a number: "))

# Reverse the number.
reverse = 0

while number > 0:
    digit = number % 10
    reverse = reverse * 10 + digit
    number //= 10

# Display the result.
print(f"Reversed number: {reverse}")