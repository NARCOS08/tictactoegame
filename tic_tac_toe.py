# Function to print the Tic-Tac-Toe board
def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

# Function to check if any player has won
def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all([spot == player for spot in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

# Function to check if the board is full (i.e., a tie)
def check_tie(board):
    return all([spot != ' ' for row in board for spot in row])

# Function to get the next player's move
def get_move(board, player):
    while True:
        try:
            move = int(input(f"Player {player}, enter your move (1-9): ")) - 1
            if board[move // 3][move % 3] == ' ':
                return move
            else:
                print("Invalid move, spot already taken.")
        except (ValueError, IndexError):
            print("Invalid input, please enter a number between 1 and 9.")

# Main game function
def play_game():
    # Initialize the board
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    
    while True:
        print_board(board)
        
        # Get the current player's move
        move = get_move(board, current_player)
        board[move // 3][move % 3] = current_player
        
        # Check if the current player has won
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check if the game is a tie
        if check_tie(board):
            print_board(board)
            print("It's a tie!")
            break
        
        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

# Run the game
play_game()
