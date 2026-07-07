# Multiply two matrices.

# Define two matrices.
matrix_one = [
    [1, 2],
    [3, 4]
]

matrix_two = [
    [5, 6],
    [7, 8]
]

# Create empty result matrix.
result = [
    [0, 0],
    [0, 0]
]

# Multiply matrices.
for row in range(len(matrix_one)):
    for column in range(len(matrix_two[0])):
        for index in range(len(matrix_two)):
            result[row][column] += (
                matrix_one[row][index] * matrix_two[index][column]
            )

# Display result.
print("Result matrix:")

for row in result:
    print(row)