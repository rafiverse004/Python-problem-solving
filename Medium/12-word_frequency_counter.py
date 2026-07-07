# Count the frequency of each word in a sentence.

# Get text from the user.
text = input("Enter a sentence: ").lower()

# Split text into words.
words = text.split()

# Store word frequency.
frequency = {}

# Count each word.
for word in words:
    if word in frequency:
        frequency[word] += 1
    else:
        frequency[word] = 1

# Display word counts.
for word, count in frequency.items():
    print(f"{word}: {count}")