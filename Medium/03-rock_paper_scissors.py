# Play the Rock Paper Scissors game against the computer.

import random

# Available choices.
choices = ["rock", "paper", "scissors"]

# Get user choice.
user_choice = input("Choose rock, paper, or scissors: ").lower()

# Generate computer choice.
computer_choice = random.choice(choices)

# Display choices.
print(f"Computer chose: {computer_choice}")

# Decide winner.
if user_choice == computer_choice:
    print("It's a tie.")
elif (
    (user_choice == "rock" and computer_choice == "scissors")
    or (user_choice == "paper" and computer_choice == "rock")
    or (user_choice == "scissors" and computer_choice == "paper")
):
    print("You win!")
else:
    print("Computer wins!")