# Check whether a string is a palindrome.

# Get a string from the user.
text = input("Enter a string: ")

# Reverse the string.
reversed_text = text[::-1]

# Compare original and reversed strings.
if text == reversed_text:
    print(f"{text} is a palindrome.")
else:
    print(f"{text} is not a palindrome.")