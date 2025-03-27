import unittest
from game_logic import gameplay

class TestSOSGame(unittest.TestCase):
    def test_general_mode_multiple_sos(self):
        """Tests multiple SOS formations in General mode with proper turn switching and scoring."""
        game = gameplay(3, "General")

        # Player 1 (Blue) places 'S'
        game.letterPlace(0, 0, 'S')
        self.assertEqual(game.scores["Blue"], 0)
        self.assertEqual(game.scores["Red"], 0)

        # Player 2 (Red) places 'O'
        game.letterPlace(0, 1, 'O')
        self.assertEqual(game.scores["Blue"], 0)
        self.assertEqual(game.scores["Red"], 0)

        # Player 1 (Blue) places 'S' and forms SOS
        winner, sos_line = game.letterPlace(0, 2, 'S')
        self.assertIsNone(winner, "General mode should not declare a winner after one SOS.")
        self.assertEqual(game.scores["Blue"], 1)
        self.assertEqual(game.scores["Red"], 0)

        # Player 2 (Red) places 'S'
        game.letterPlace(1, 0, 'S')

        # Player 1 (Blue) places 'O'
        game.letterPlace(1, 1, 'O')

        # Player 2 (Red) places 'S' and forms SOS
        winner, sos_line = game.letterPlace(1, 2, 'S')
        self.assertIsNone(winner, "General mode should continue until the board is full.")
        self.assertEqual(game.scores["Blue"], 1)
        self.assertEqual(game.scores["Red"], 1)

        # Test game continues correctly
        game.letterPlace(2, 0, 'S')
        game.letterPlace(2, 1, 'O')
        winner, sos_line = game.letterPlace(2, 2, 'S')  # Should form another SOS

        self.assertIsNone(winner, "Game should still be ongoing.")
        self.assertEqual(game.scores["Blue"], 2)
        self.assertEqual(game.scores["Red"], 1)

        # Ensure no premature winner declaration
        self.assertIsNone(game.checkWinnerScore(), "Winner should not be determined until the board is full.")

if __name__ == "__main__":
    unittest.main()