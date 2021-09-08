'''
Define nodes of search tree and vanilla bfs search algorithm

Author: Tony Lindgren
'''

import queue
from time import process_time

"""
todo 
- how to use proces_time to get processing time
- How to calculate effective branching factor - See assignment notes
"""


class Node:
    """
    This class defines nodes in search trees. It keep track of:
    state, cost, parent, action, and depth
    """

    def __init__(self, state, cost=0, parent=None, action=None):
        self.parent = parent
        self.state = state
        self.action = action
        self.cost = cost
        self.depth = 0
        if parent:
            self.depth = parent.depth + 1

        self.action_state_map = dict()

    def goal_state(self):
        return self.state.check_goal()

    def successor(self):
        successors = queue.Queue()
        for action in self.state.action:
            child = self.state.move(action)
            if child != None:
                childNode = Node(child, self.cost + 1, self, action)
                successors.put(childNode)
                self.action_state_map[childNode.action] = childNode.state
        return successors

    def pretty_print_solution(self, verbose=False) -> None:
        """
        Prints out the actions needed to go from start to goal
        If verbose is set to true, both the actions and states will be printed.
        """
        for action, state in self.action_state_map.items():
            print(f"Printing solution with verbosity set to {verbose}")
            if not verbose:
                print(f"action: {action}\n")
            else:
                print(f"-----------------\naction: {action}")
                print("------------------------------------")
                print(state)
                print("------------------------------------")


class SearchAlgorithm:
    """
    Class for search algorithms, call it with a defined problem
    """

    # number_of_nodes_traversed = 0  # This is the cost for the solution

    def __init__(self, problem):
        self.start = Node(problem)
        self.statistics = {}
        self.start_time = 0

    def bfs(self):
        frontier = queue.Queue()
        frontier.put(self.start)
        stop = False
        reached = set()
        while not stop:
            if frontier.empty():
                return None
            curr_node = frontier.get()
            if curr_node.goal_state():
                stop = True
                return curr_node

            successor = curr_node.successor()
            while not successor.empty():
                if successor.get() not in reached:
                    reached.add(successor.get())
                    frontier.put(successor.get())

    #def print_statistics(self):
        """
        Inform the user about
        - depth,
        - search cost (number of nodes generated),
        - cost for functions (number of nodes in path from root to goal),
        - cpu time consumed
        - effective branching factor (= N^1/d), N=number of nodes, d=depth
        """
