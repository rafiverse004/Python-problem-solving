# Perform basic arithmetic operations using two numbers.

# Get input from the user.
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /): ")

# Perform the selected operation.
if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/":
    if second_number != 0:
        result = first_number / second_number
    else:
        result = "Cannot divide by zero."
else:
    result = "Invalid operator."

# Display the result.
print(f"Result: {result}")