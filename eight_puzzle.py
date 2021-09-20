"""
Eight puzzle solver
@author Bernard Longho, Mba Godwin
"""


class EightPuzzle:
    """
    An 8-puzzle solver 
    """

    def __init__(self, initial_state, goal):
        self.state = initial_state
        self.goal = goal
        # The different possible directions to move
        self.action = ["up", "down", "left", "right"]

