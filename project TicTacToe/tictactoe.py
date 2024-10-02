# Tic Tac Toe game in Python

# Function to print the Tic Tac Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if a player has won
def check_win(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

# Function to check if the board is full
def check_full(board):
    return all([cell != " " for row in board for cell in row])

# Function to get the player's move
def get_move(player):
    while True:
        try:
            row = int(input(f"Player {player}, enter the row (0, 1, or 2): "))
            col = int(input(f"Player {player}, enter the column (0, 1, or 2): "))
            if row in range(3) and col in range(3):
                return row, col
            else:
                print("Invalid input. Please enter numbers between 0 and 2.")
        except ValueError:
            print("Invalid input. Please enter numbers.")

# Main function to play the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    while True:
        print_board(board)
        row, col = get_move(current_player)
        
        if board[row][col] == " ":
            board[row][col] = current_player
            if check_win(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif check_full(board):
                print_board(board)
                print("It's a tie!")
                break
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Cell already taken. Try again.")

if __name__ == "__main__":
    play_game()
