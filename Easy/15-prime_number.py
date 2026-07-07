# Check whether a number is prime or not.

# Get a number from the user.
number = int(input("Enter a number: "))

# Assume the number is prime.
is_prime = True

# Check divisibility.
if number <= 1:
    is_prime = False
else:
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
            break

# Display the result.
if is_prime:
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")