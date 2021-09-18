"""
Define nodes of search tree and vanilla bfs search algorithm

__author__: Tony Lindgren, Longho Bernard Che, Mba Godwin
"""
import queue
import time

from utils import RunningStats


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
        return [[node.action, node.state.state] for node in path[::-1][1:]]

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

    def __str__(self) -> str:
        return "Node[state={}, cost={}, action={}, parent={}".format(self.state, self.cost, self.action, self.parent)


class SearchAlgorithm:
    """
    Class for search algorithms, call it with a defined problem
    """

    def __init__(self, problem, check_visited_nodes=False):
        self.start = Node(problem)
        self.running_stats = None
        self.check_explored_nodes = check_visited_nodes

    def bfs(self, statistics=False):
        start_time = time.process_time()
        frontier = queue.Queue()
        frontier.put(self.start)
        explored = []
        stop = False
        while not stop:
            if frontier.empty():
                return None
            curr_node = frontier.get()
            if self.check_explored_nodes:
                explored.append(curr_node)
            if curr_node.goal_state():
                stop = True
                if statistics:
                    stop_time = time.process_time()
                    cpu_time = stop_time - start_time
                    nodes_explored = len(explored) if self.check_explored_nodes else frontier.qsize()
                    self.running_stats = RunningStats(search="bfs", duration=cpu_time, depth=curr_node.depth,
                                                      nodes=nodes_explored, cost=curr_node.cost)
                return curr_node

            successor = curr_node.successor()
            while not successor.empty():
                child_node = successor.get()
                if self.check_explored_nodes:
                    if child_node not in explored:
                        frontier.put(child_node)
                else:
                    frontier.put(child_node)

    def statistics(self) -> None:
        """
         If statistics printing is enabled, print the statistics. Otherwise, nothing is printed.
        """
        if self.running_stats is not None:
            print(f"\n{33 * '>'}\n"
                  f"Statistics for {self.running_stats.algorithm.upper()} with check for explored nodes"
                  f" {'ENABLED' if self.check_explored_nodes else 'DISABLED'}", self.running_stats)
