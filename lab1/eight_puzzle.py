"""
Eight puzzle solver
@author Bernard Longho, Mba Godwin
"""
import utils


class EightPuzzle:
    """
    An 8-puzzle solver 
    """

    def __init__(self, initial_state, goal):
        self.state = initial_state
        self.goal = goal
        # The different possible directions to move
        self.action = ["up", "down", "left", "right"]

    def check_goal(self):
        return self.state == self.goal

    def h_1(self):
        """Heuristics that calculates the number of tiles out of place

        Returns(int): the number of tiles out of place
        """
        # Go through current state and check for and count the number of tiles out of place

        num_tiles_out_of_place = 0
        for row in range(3):
            for col in range(3):
                if self.state[row][col] != 'e' and self.state[row][col] != self.goal[row][col]:
                    num_tiles_out_of_place += 1

        return num_tiles_out_of_place

    def h_2(self):
        """Calculate the Manhattan distance

        Returns: The manhattan distance
        -------

        """
        m_distance = 0
        for row in range(3):
            for col in range(3):
                entry = self.state[row][col]
                if entry != 'e':
                    goal_row, goal_col = self._calculated_expected_goal_position(entry)
                    m_distance += abs(goal_row - row) + abs(goal_col - col)

        return m_distance

    def _is_solvable(self):
        inversion = 0
        flattened_state = utils.flatten(self.state)
        for i in range(len(flattened_state)):
            for j in range(i + 1, len(flattened_state)):
                if flattened_state[i] != 'e' and flattened_state[j] != 'e' and flattened_state[i] > flattened_state[j]:
                    inversion += 1

        return inversion % 2 == 0

    def empty_position(self):
        for idx, row in enumerate(self.state):
            for jdx, col in enumerate(row):
                if col == 'e':
                    return idx, jdx
        return None

    def _calculated_expected_goal_position(self, entry):
        for row in range(3):
            for col in range(3):
                if self.goal[row][col] == entry:
                    return row, col
        return None

    def pretty_print(self):
        delim = "|"
        for idx, row in enumerate(self.state):
            if self.state[idx][0] == 'e':
                self.state[idx][0] = ' '
            print("-" * 13)
            print(delim, self.state[idx][0], delim, self.state[idx][1], delim,
                  self.state[idx][2], delim)
        print("-" * 13)
