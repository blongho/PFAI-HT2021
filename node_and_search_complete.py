"""
Define nodes of search tree and vanilla bfs search algorithm

__author__: Tony Lindgren, Longho Bernard Che, Mbah Edwin
"""
import queue


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
            if child is not None:
                childNode = Node(child, self.cost + 1, self, action)
                successors.put(childNode)
        return successors

    def get_solution_path(self):
        """
        Retrieve the solution path in a reversed fashion
        """
        node, path = self, []
        while node:
            path.append(node)
            node = node.parent
        return [[node.action, node.state.state] for node in list(reversed(path))[1:]]

    def pretty_print_solution(self, verbose=False):
        """
        Prints out the actions needed to go from start to goal
        If verbose is set to true, both the actions and states will be printed.
        """
        path = self.get_solution_path()
        for action in path:
            print(f"action: {action[0]}")
            if verbose:
                print("----------------------------")
                print(" #miss on left bank: ", action[1][0][0])
                print(" #cann on left bank: ", action[1][0][1])
                print("            boat is: ", action[1][1])
                print("#miss on right bank: ", action[1][2][0])
                print("#cann on right bank: ", action[1][2][1])
                print("----------------------------")


class SearchAlgorithm:
    """
    Class for search algorithms, call it with a defined problem
    """

    def __init__(self, problem):
        self.start = Node(problem)
        self.reached = {}  # A dictionary to hold the node and state

    def bfs(self):
        frontier = queue.Queue()
        frontier.put(self.start)
        stop = False
        while not stop:
            if frontier.empty():
                return None
            curr_node = frontier.get()
            if curr_node not in self.reached:
                self.reached[curr_node.action] = curr_node
            if curr_node.goal_state():
                stop = True
                return curr_node

            successor = curr_node.successor()
            while not successor.empty():
                # if successor.get() not in reached.items():
                frontier.put(successor.get())
