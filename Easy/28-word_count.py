# Count the number of words in a sentence.

# Get a sentence from the user.
sentence = input("Enter a sentence: ")

# Split the sentence into words.
words = sentence.split()

# Count the words.
word_count = len(words)

# Display the result.
print(f"Number of words: {word_count}")