import unittest
from game_logic import gameplay

class TestSOSGame(unittest.TestCase):
    def test_simple_mode(self):
        game = gameplay(3, mode="Simple")

        # Make moves that lead to an SOS
        winner, _ = game.letterPlace(0, 0, 'S')
        if winner:  # If the game already ended, assert the winner dynamically
            self.assertEqual(winner, game.current_turn, "First SOS should determine the winner.")
            return
        
        game.switch_turn()
        winner, _ = game.letterPlace(0, 1, 'O')
        if winner:
            self.assertEqual(winner, game.current_turn)
            return

        game.switch_turn()
        winner, _ = game.letterPlace(0, 2, 'S')
        
        # Assert whoever won was the first to form an SOS
        self.assertEqual(winner, game.current_turn, "First SOS should determine the winner.")

if __name__ == "__main__":
    unittest.main()
