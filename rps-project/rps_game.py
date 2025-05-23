import unittest
from rps_game import decide_winner, get_computer_choice, is_valid_choice

class TestRPSGame(unittest.TestCase):
    def test_user_wins(self):
        self.assertEqual(decide_winner("rock", "scissors"), "win")
        self.assertEqual(decide_winner("paper", "rock"), "win")
        self.assertEqual(decide_winner("scissors", "paper"), "win")

    def test_user_loses(self):
        self.assertEqual(decide_winner("rock", "paper"), "lose")
        self.assertEqual(decide_winner("paper", "scissors"), "lose")
        self.assertEqual(decide_winner("scissors", "rock"), "lose")

    def test_tie(self):
        self.assertEqual(decide_winner("rock", "rock"), "tie")
        self.assertEqual(decide_winner("paper", "paper"), "tie")
        self.assertEqual(decide_winner("scissors", "scissors"), "tie")

    def test_valid_input(self):
        self.assertTrue(is_valid_choice("rock"))
        self.assertTrue(is_valid_choice("paper"))
        self.assertTrue(is_valid_choice("scissors"))
        self.assertTrue(is_valid_choice("ROCK"))
        self.assertTrue(is_valid_choice("  paper  "))

    def test_invalid_input(self):
        self.assertFalse(is_valid_choice("banana"))
        self.assertFalse(is_valid_choice("123"))
        self.assertFalse(is_valid_choice("@!#"))
        self.assertFalse(is_valid_choice("rock!"))
        self.assertFalse(is_valid_choice(None))
        self.assertFalse(is_valid_choice([]))
        self.assertFalse(is_valid_choice(123))

    def test_computer_choice_is_valid(self):
        for _ in range(100):
            self.assertIn(get_computer_choice(), ["rock", "paper", "scissors"])

if __name__ == '__main__':
    unittest.main()

