# Create a simple text-based adventure game.

# Starting location.
location = "forest"

print("You are lost in a forest.")

# Player choices.
choice = input(
    "You see a cave and a river. "
    "Choose cave or river: "
).lower()

# Game logic.
if choice == "cave":
    print("You found a hidden treasure!")
elif choice == "river":
    print("You found a boat and escaped safely.")
else:
    print("You stayed in the forest and got lost.")

print("Game over.")