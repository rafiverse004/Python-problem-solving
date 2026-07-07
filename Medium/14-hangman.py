# Create a simple Hangman word guessing game.

# Store the secret word.
secret_word = "python"

# Create empty guessed letters.
guessed_letters = []

# Set number of attempts.
attempts = 6

while attempts > 0:
    display_word = ""

    # Show guessed progress.
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print(f"\nWord: {display_word}")

    # Check if user completed the word.
    if display_word == secret_word:
        print("You won!")
        break

    # Get user's guess.
    guess = input("Guess a letter: ").lower()

    if guess in secret_word:
        guessed_letters.append(guess)
        print("Correct guess.")
    else:
        attempts -= 1
        print(f"Wrong guess. Attempts left: {attempts}")

else:
    print(f"You lost. The word was {secret_word}.")