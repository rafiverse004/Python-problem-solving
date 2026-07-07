# Create a game where the user guesses a randomly generated number.

import random

# Generate a random number.
secret_number = random.randint(1, 100)

# Get user's guess.
guess = int(input("Guess a number between 1 and 100: "))

# Check the guess.
if guess == secret_number:
    print("Congratulations! You guessed the correct number.")
elif guess < secret_number:
    print(f"Wrong guess. The number was {secret_number}. Try higher.")
else:
    print(f"Wrong guess. The number was {secret_number}. Try lower.")