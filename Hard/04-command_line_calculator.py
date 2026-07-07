# Create a calculator using command-line arguments.

import sys

# Check arguments.
if len(sys.argv) != 4:
    print("Usage: python calculator.py number operator number")
else:
    first_number = float(sys.argv[1])
    operator = sys.argv[2]
    second_number = float(sys.argv[3])

    # Perform calculation.
    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "/":
        result = first_number / second_number
    else:
        result = "Invalid operator"

    # Display result.
    print(f"Result: {result}")