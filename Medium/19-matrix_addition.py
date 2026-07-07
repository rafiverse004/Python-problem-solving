# Add two matrices of the same size.

# Define two matrices.
matrix_one = [
    [1, 2],
    [3, 4]
]

matrix_two = [
    [5, 6],
    [7, 8]
]

# Store result matrix.
result = []

# Add corresponding elements.
for row in range(len(matrix_one)):
    new_row = []

    for column in range(len(matrix_one[0])):
        value = matrix_one[row][column] + matrix_two[row][column]
        new_row.append(value)

    result.append(new_row)

# Display result.
print("Result matrix:")

for row in result:
    print(row)