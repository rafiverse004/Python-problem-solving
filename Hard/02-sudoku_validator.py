# Validate whether a Sudoku board is valid.

# Example Sudoku board.
board = [
    [5, 3, 4, 6, 7, 8, 9, 1, 2],
    [6, 7, 2, 1, 9, 5, 3, 4, 8],
    [1, 9, 8, 3, 4, 2, 5, 6, 7],
    [8, 5, 9, 7, 6, 1, 4, 2, 3],
    [4, 2, 6, 8, 5, 3, 7, 9, 1],
    [7, 1, 3, 9, 2, 4, 8, 5, 6],
    [9, 6, 1, 5, 3, 7, 2, 8, 4],
    [2, 8, 7, 4, 1, 9, 6, 3, 5],
    [3, 4, 5, 2, 8, 6, 1, 7, 9],
]


# Check rows and columns.
def check_rows_columns():
    for i in range(9):
        row = set(board[i])
        column = set(board[j][i] for j in range(9))

        if len(row) != 9 or len(column) != 9:
            return False

    return True


# Check 3x3 boxes.
def check_boxes():
    for row in range(0, 9, 3):
        for column in range(0, 9, 3):
            numbers = []

            for i in range(3):
                for j in range(3):
                    numbers.append(board[row + i][column + j])

            if len(set(numbers)) != 9:
                return False

    return True


# Validate Sudoku.
if check_rows_columns() and check_boxes():
    print("Valid Sudoku.")
else:
    print("Invalid Sudoku.")