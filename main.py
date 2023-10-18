# Initialize an empty 3x3 Tic-Tac-Toe board
board = [[" " for _ in range(3)] for _ in range(3)]


# Function to print the Tic-Tac-Toe board
def print_board():
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


# Function to check if someone has won
def check_win(player):
    # Check rows and columns for a win
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True

    # Check diagonals for a win
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False


# Function to check if the board is full (a tie)
def is_full():
    return all(cell != ' ' for row in board for cell in row)


# The main game loop
def main():
    current_player = "X"

    while True:
        print_board()

        # Get the player's move
        try:
            move = input(f"Player {current_player}, enter your move (row, column): ")
            row, col = map(int, move.split(","))
        except (ValueError, IndexError):
            print("Invalid input. Please enter your move in the format 'row, column'.")
            continue

        if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
            board[row][col] = current_player
        else:
            print("Invalid move. Try again.")
            continue

        if check_win(current_player):
            print_board()
            print(f"Player {current_player} wins! Congratulations!")
            break

        if is_full():
            print_board()
            print("It's a tie! No one wins.")
            break

        current_player = "O" if current_player == "X" else "X"  # Switch to the other player


if __name__ == "__main__":
    main()
