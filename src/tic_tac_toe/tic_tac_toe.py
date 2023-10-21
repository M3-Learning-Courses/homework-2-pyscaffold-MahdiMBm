import random
import pyfiglet

def select_difficulty():
    """Select the difficulty level for the game.

    Returns:
        str: The selected difficulty level ("1" for Easy or "2" for Hard).
    """
    while True:
        print("Select the difficulty level:")
        print("1. Easy")
        print("2. Hard")
        choice = input("Enter your choice (1 or 2): ")
        if choice in ("1", "2"):
            return choice
        else:
            print("Invalid choice. Please enter 1 for Easy or 2 for Hard.")

def print_board(board):
    """Print the current game board.

    Args:
        board (list): A 2D list representing the game board.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_win(board, player):
    """Check if a player has won the game.

    Args:
        board (list): A 2D list representing the game board.
        player (str): The player's symbol ("X" or "O").

    Returns:
        bool: True if the player has won, False otherwise.
    """
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

def is_board_full(board):
    """Check if the game board is full (a tie).

    Args:
        board (list): A 2D list representing the game board.

    Returns:
        bool: True if the board is full, False otherwise.
    """
    return all(cell != " " for row in board for cell in row)

def get_move():
    """Get the player's move input.

    Returns:
        int: The selected move (an integer between 1 and 9).
    """
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if 1 <= move <= 9:
                return move
            else:
                print("Invalid input. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9.")

def analyze_board(board, player):
    """Analyze the board to find potential wins or blocks for a player.

    Args:
        board (list): A 2D list representing the game board.
        player (str): The player's symbol ("X" or "O").

    Returns:
        tuple: A tuple (row, col) representing a potential move for the player or None if no moves are found.
    """
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

def ai_move_easy(board):
    """Make a move for the AI in easy difficulty.

    Args:
        board (list): A 2D list representing the game board.

    Returns:
        tuple: A tuple (row, col) representing the AI's move.
    """
    empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]
    if empty_cells:
        return random.choice(empty_cells)
    else:
        return (-1, -1)


#


def ai_move_hard(board):
    """Make a move for the AI in hard difficulty.

    Args:
        board (list): A 2D list representing the game board.

    Returns:
        tuple: A tuple (row, col) representing the AI's move.
    """
    win_move = analyze_board(board, "O")
    block_move = analyze_board(board, "X")

    if win_move:
        return win_move
    elif block_move:
        return block_move
    else:
        available_moves = [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]
        center = (1, 1)
        corners = [(0, 0), (0, 2), (2, 0), (2, 2)]
        edges = [(0, 1), (1, 0), (1, 2), (2, 1)]

        for move in [center] + corners + edges:
            if move in available_moves:
                return move

def play_game():
    """Play_game, allowing the player to choose the difficulty level.

    The game begins by prompting the player to select a difficulty level, and then it proceeds to alternate
    between the player and the AI, allowing each to make moves until a win or a tie occurs. The game result
    is displayed, and the player is given the option to play again.


    Returns:
        result of the game 
    """
    print("Welcome to Tic-Tac-Toe!")
    difficulty = select_difficulty()

    while True:
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
                if current_player == "X":
                    text = "You Win!"
                    font = pyfiglet.Figlet(font='standard')
                    stylized_text = font.renderText(text)
                    print(stylized_text)
                else:
                    text = "You Lose!"
                    font = pyfiglet.Figlet(font='standard')
                    stylized_text = font.renderText(text)
                    print(stylized_text)
                break

            if is_board_full(board):
                print_board(board)
                print("It's a tie!")
                text = "Tie!"
                font = pyfiglet.Figlet(font='standard')
                stylized_text = font.renderText(text)
                print(stylized_text)
                break

            if current_player == "O":
                empty_cells = [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]
                if len(empty_cells) == 1:
                    print_board(board)
                    print("Only one move left. It's a tie!")
                    text = "Tie!"
                    font = pyfiglet.Figlet(font='standard')
                    stylized_text = font.renderText(text)
                    print(stylized_text)
                    break

            current_player = "O" if current_player == "X" else "X"

        replay = input("Do you want to play again? (yes or no): ").lower()
        if replay != "yes":
            break

if __name__ == "__main__":
    play_game()