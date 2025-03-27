import unittest
from game_logic import SimpleGame, GeneralGame


class TestSOSGame(unittest.TestCase):
    def test_simple_mode(self):
        game = SimpleGame(3)

        # Make moves that lead to an SOS
        winner, _ = game.letterPlace(0, 0, 'S')
        if winner:  
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
