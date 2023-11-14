import unittest
# import pyfiglet
# import os

# Set the 'APPDATA' environment variable to your 'Roaming' directory
# os.environ['APPDATA'] = r'C:\Users\98913\AppData\Roaming'
from unittest.mock import patch
import os


from io import StringIO
from tic_tac_toe.tic_tac_toe import select_difficulty, check_win, is_board_full, get_move, analyze_board, ai_move_easy, ai_move_hard


class TestTicTacToe(unittest.TestCase):
    def test_select_difficulty(self):
        with patch("builtins.input", side_effect=["1"]):
            result = select_difficulty()
            self.assertEqual(result, "1")

        with patch("builtins.input", side_effect=["2"]):
            result = select_difficulty()
            self.assertEqual(result, "2")
    def test_check_win(self):
        board = [
            ["X", "O", "X"],
            ["O", "X", "O"],
            ["X", "X", "O"],
        ]
        self.assertTrue(check_win(board, "X"))

        board = [
            ["X", "O", "X"],
            ["O", "O", "X"],
            ["X", "X", "O"],
        ]
        self.assertFalse(check_win(board, "X"))

    def test_is_board_full(self):
        board = [
            ["X", "O", "X"],
            ["O", "X", "O"],
            ["X", "X", "O"],
        ]
        self.assertTrue(is_board_full(board))

        board = [
            ["X", "O", "X"],
            ["O", "O", "X"],
            ["X", "X", " "],
        ]
        self.assertFalse(is_board_full(board))

    def test_get_move(self):
        with patch("builtins.input", side_effect=["1"]):
            result = get_move()
            self.assertEqual(result, 1)
    def test_get_move(self):
        with patch("builtins.input", side_effect=["2"]):
            result = get_move()
            self.assertEqual(result, 2)            

        with patch("builtins.input", side_effect=["5"]):
            result = get_move()
            self.assertEqual(result, 5)

    def test_analyze_board(self):
        board = [
            ["X", "O", "X"],
            ["O", " ", "X"],
            ["X", "X", "O"],
        ]
        result = analyze_board(board, "X")
        self.assertEqual(result, (1, 1))

    def test_ai_move_easy(self):
        board = [
            ["X", "O", "X"],
            ["O", " ", "X"],
            ["X", "X", "O"],
        ]
        result = ai_move_easy(board)
        self.assertIn(result, [(1, 1), (1, 3), (2, 1)])

    def test_ai_move_hard(self):
        board = [
            ["X", "O", "X"],
            ["O", " ", "X"],
            ["X", "X", "O"],
        ]
        result = ai_move_hard(board)
        self.assertIn(result, [(1, 1), (1, 2), (2, 1)])
# ... (previous test cases) ...


if __name__ == "__main__":
    unittest.main()