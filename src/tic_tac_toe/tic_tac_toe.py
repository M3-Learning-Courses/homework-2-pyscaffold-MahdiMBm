import random

# Function for the player to select the difficulty level
def select_difficulty():
    while True:
        print("Select the difficulty level:")
        print("1. Easy")
        print("2. Hard")
        choice = input("Enter your choice (1 or 2): ")
        if choice in ("1", "2"):
            return choice
        else:
            print("Invalid choice. Please enter 1 for Easy or 2 for Hard.")

# Function to print the game board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check if a player has won the game
def check_win(board, player):
    # Check rows and columns for a win
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    # Check diagonals for a win
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Function to check if the game board is full (a tie)
def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

# Function to get the player's move input
def get_move():
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if 1 <= move <= 9:
                return move
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

# Function to analyze the board and find potential wins or blocks for a player
def analyze_board(board, player):
    for row in range(3):
        # Check for potential wins or blocks in rows
        if board[row].count(player) == 2 and board[row].count(" ") == 1:
            col = board[row].index(" ")
            return row, col

    for col in range(3):
        # Check for potential wins or blocks in columns
        if [board[row][col] for row in range(3)].count(player) == 2 and [board[row][col] for row in range(3)].count(" ") == 1:
            row = [board[row][col] for row in range(3)].index(" ")
            return row, col

    # Check for potential wins or blocks in diagonals
    if [board[i][i] for i in range(3)].count(player) == 2 and [board[i][i] for i in range(3)].count(" ") == 1:
        index = [board[i][i] for i in range(3)].index(" ")
        return index, index

    if [board[i][2 - i] for i in range(3)].count(player) == 2 and [board[i][2 - i] for i in range(3)].count(" ") == 1:
        index = [board[i][2 - i] for i in range(3)].index(" ")
        return index, 2 - index

    return None

# Function for the AI to make a move (easy difficulty)
def ai_move_easy(board):
    # Randomly select an available move for the AI
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]
    return random.choice(empty_cells)

# Function for the AI to make a move (hard difficulty)
def ai_move_hard(board):
    # Check for potential wins or blocks before making a move
    win_move = analyze_board(board, "O")
    block_move = analyze_board(board, "X")

    if win_move:
        return win_move
    elif block_move:
        return block_move
    else:
        # Strategy for hard mode: prioritize center, corners, then edges
        available_moves = [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]
        center = (1, 1)
        corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
        edges = [(0, 1), (1, 0), (1, 2), (2, 1)]

        for move in [center] + corners + edges:
            if move in available_moves:
                return move

# Function to play the game
def play_game():
    print("Welcome to Tic-Tac-Toe!")
    difficulty = select_difficulty()

    while True:
        # Randomly select the starting player between "Player" and "AI"
        starting_player = random.choice(["Player", "AI"])

        print(f"Starting the game. {starting_player} goes first.")
        board = [[" " for _ in range(3)] for _ in range(3)]
        players = {
            "X": "Player",
            "O": "AI"
        }
        current_player = "X" if starting_player == "Player" else "O"

        while True:
            print_board(board)

            if current_player == "X":
                move = get_move()
                row = (move - 1) // 3
                col = (move - 1) % 3
            else:
                print(f"{players[current_player]} is thinking...")
                if difficulty == "1":
                    row, col = ai_move_easy(board)
                else:
                    row, col = ai_move_hard(board)
                move = row * 3 + col + 1

            if board[row][col] == " ":
                board[row][col] = current_player
            else:
                print("Invalid move. That spot is already taken. Try again.")
                continue

            if check_win(board, current_player):
                print_board(board)
                print(f"{players[current_player]} wins!")
                break

            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break

            if current_player == "O":
                empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]
                if len(empty_cells) == 1:
                    print_board(board)
                    print("Only one move left. It's a tie!")
                    break

            current_player = "O" if current_player == "X" else "X"

        replay = input("Do you want to play again? (yes or no): ").lower()
        if replay != "yes":
            break

if __name__ == "__main__":
    play_game()
