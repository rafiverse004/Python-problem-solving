# Analyze a text file by counting lines, words, and characters.

# Get file name from the user.
file_name = input("Enter file name: ")

try:
    # Open and read the file.
    with open(file_name, "r") as file:
        content = file.read()

    # Analyze file content.
    lines = content.split("\n")
    words = content.split()

    line_count = len(lines)
    word_count = len(words)
    character_count = len(content)

    # Display results.
    print(f"Lines: {line_count}")
    print(f"Words: {word_count}")
    print(f"Characters: {character_count}")

except FileNotFoundError:
    print("File not found.")