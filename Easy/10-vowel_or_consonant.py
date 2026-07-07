# Check whether a character is a vowel or consonant.

# Get a character from the user.
character = input("Enter a character: ").lower()

# Check if the character is a vowel.
if character in "aeiou":
    print(f"{character} is a vowel.")
else:
    print(f"{character} is a consonant.")