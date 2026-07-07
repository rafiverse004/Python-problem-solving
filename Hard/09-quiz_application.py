# Create a quiz application.

# Store questions and answers.
questions = {
    "What is the capital of France? ": "paris",
    "What is 2 + 2? ": "4",
    "What language are we learning? ": "python"
}

score = 0

# Ask questions.
for question, answer in questions.items():
    user_answer = input(question).lower()

    if user_answer == answer:
        score += 1
        print("Correct!")
    else:
        print("Wrong answer.")

# Display final score.
print(f"Your score: {score}/{len(questions)}")