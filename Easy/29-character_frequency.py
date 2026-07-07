# Count the frequency of each character in a string.

# Get a string from the user.
text = input("Enter a string: ")

# Store character frequencies.
frequency = {}

# Count each character.
for character in text:
    if character in frequency:
        frequency[character] += 1
    else:
        frequency[character] = 1

# Display the result.
for character, count in frequency.items():
    print(f"{character}: {count}")