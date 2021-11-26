import unittest

from eight_puzzle import EightPuzzle


class TestEightPuzzle(unittest.TestCase):
    init_state = [[7, 2, 4], [5, 'e', 6], [8, 3, 1]]
    goal_state = [['e', 1, 2], [3, 4, 5], [6, 7, 8]]

    def setUp(self) -> None:
        self.eight_puzzle = EightPuzzle(initial_state=self.init_state, goal=self.goal_state)

    def test_h1(self):
        self.assertEqual(self.eight_puzzle.h_1(), 8, "The number of tiles out of place should be 8")

    def test_h2(self):
        self.assertEqual(self.eight_puzzle.h_2(), 18, "The manhattan distance should be 18")

    def test_goal_state(self):
        self.assertEqual(self.eight_puzzle.check_goal(), False, "The goal state should return false")

        self.eight_puzzle = EightPuzzle(initial_state=self.goal_state, goal=self.goal_state)

        self.assertEqual(self.eight_puzzle.check_goal(), True, "The goal state should be true")


if __name__ == '__main__':
    unittest.main()
