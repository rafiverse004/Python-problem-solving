# Calculate student grades based on marks.

# Get marks from the user.
marks = float(input("Enter student marks: "))

# Determine grade.
if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
elif marks >= 60:
    grade = "D"
else:
    grade = "F"

# Display result.
print(f"Grade: {grade}")