# Create a two-player Tic-Tac-Toe game.

# Create the game board.
board = [" " for _ in range(9)]

# Display the board.
def display_board():
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()


# Check winner.
def check_winner(player):
    winning_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]

    for position in winning_positions:
        if (
            board[position[0]] == player
            and board[position[1]] == player
            and board[position[2]] == player
        ):
            return True

    return False


# Start the game.
current_player = "X"

for _ in range(9):
    display_board()

    move = int(input(f"Player {current_player}, choose position (1-9): ")) - 1

    if board[move] == " ":
        board[move] = current_player
    else:
        print("Position already taken.")
        continue

    if check_winner(current_player):
        display_board()
        print(f"Player {current_player} wins!")
        break

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

else:
    display_board()
    print("It's a draw.")