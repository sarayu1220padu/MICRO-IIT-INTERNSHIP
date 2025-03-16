def print_board(board):
    # Display the Tic-Tac-Toe board
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_winner(board, player):
    # Check for a winner
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    # Check if the board is full
    return all(cell != " " for row in board for cell in row)

def tic_tac_toe():
    # Initialize the board and scores
    board = [[" " for _ in range(3)] for _ in range(3)]
    scores = {"X": 0, "O": 0}
    current_player = "X"

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")

        # Get the player's move
        while True:
            try:
                row = int(input("Enter row (0, 1, 2): "))
                col = int(input("Enter column (0, 1, 2): "))
                if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == " ":
                    break
                else:
                    print("Invalid move! Try again.")
            except ValueError:
                print("Invalid input! Please enter numbers.")

        # Update the board
        board[row][col] = current_player

        # Check for a winner
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            scores[current_player] += 1
            break

        # Check for a draw
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = "O" if current_player == "X" else "X"

    # Display scores
    print(f"Scores - Player X: {scores['X']}, Player O: {scores['O']}")

    # Ask if the players want to play again
    replay = input("Do you want to play again? (yes/no): ").lower()
    if replay == "yes":
        tic_tac_toe()
    else:
        print("Thanks for playing! Have a nice day !")

# Run the game
if __name__ == "__main__":
    print("Welcome to Tic-Tac-Toe!")
    tic_tac_toe()
