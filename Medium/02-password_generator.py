# Generate a random password with letters, numbers, and symbols.

import random
import string

# Get password length.
length = int(input("Enter password length: "))

# Create available characters.
characters = string.ascii_letters + string.digits + string.punctuation

# Generate password.
password = ""

for _ in range(length):
    password += random.choice(characters)

# Display the password.
print(f"Generated password: {password}")