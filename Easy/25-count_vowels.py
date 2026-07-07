# Count the number of vowels in a string.

# Get a string from the user.
text = input("Enter a string: ").lower()

# Count vowels.
vowel_count = 0

for character in text:
    if character in "aeiou":
        vowel_count += 1

# Display the result.
print(f"Number of vowels: {vowel_count}")