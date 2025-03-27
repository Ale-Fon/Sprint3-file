import unittest
from game_logic import SimpleGame, GeneralGame


class TestSOSGame(unittest.TestCase):
   def test_general_mode(self):
        game = GeneralGame(3)

        # Make moves that create multiple SOS occurrences
        game.letterPlace(0, 0, 'S')
        game.letterPlace(0, 1, 'O')
        winner, _ = game.letterPlace(0, 2, 'S')  # First SOS
        self.assertIsNone(winner, "Winner should not be declared mid-game.")

        game.letterPlace(1, 0, 'S')
        game.letterPlace(1, 1, 'O')
        winner, _ = game.letterPlace(1, 2, 'S')  # Second SOS
        self.assertIsNone(winner, "Winner should not be declared mid-game.")

        game.letterPlace(2, 0, 'S')
        game.letterPlace(2, 1, 'O')
        winner, _ = game.letterPlace(2, 2, 'S')  # Third SOS, board full

        # **At this point, the board should be full, so a winner should be declared**
        final_winner = game.checkWinnerScore()
        self.assertIn(final_winner, ["Blue", "Red", "Draw"], "Final winner should be determined correctly.")

if __name__ == "__main__":
    unittest.main()
