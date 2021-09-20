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

    def get_state(self):
        return self.state

    def goal_state(self):
        return self.state.check_goal()

    def successor(self, queue_type=queue.Queue()):
        """
        All the child nodes from a current node
        Parameters
        ----------
        queue_type the type of queue to be used [fifo|lifo]

        Returns a queue containing the nodes that are children to the current node
        -------

        """
        successors = queue_type
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
            print("action: ", action[0])
            if verbose:
                print("----------------------------")
                print(" #miss on left bank: ", action[1][0][0])
                print(" #cann on left bank: ", action[1][0][1])
                print("            boat is: ", action[1][1])
                print("#miss on right bank: ", action[1][2][0])
                print("#cann on right bank: ", action[1][2][1])
                print("----------------------------")

    def __str__(self) -> str:
        return "Node[state={}, cost={}, action={}".format(self.state, self.cost, self.action)


class SearchAlgorithm:
    """
    Class for search algorithms, call it with a defined problem
    """

    def __init__(self, problem, check_visited_nodes=False):
        self.start = Node(problem)
        self.running_stats = None
        self.check_visited_nodes = check_visited_nodes

    def bfs(self, statistics=False):
        start_time = time.process_time() if statistics else None
        frontier = queue.Queue()
        frontier.put(self.start)
        explored = [self.start.state]
        stop = False
        while not stop:
            if frontier.empty():
                return None
            curr_node = frontier.get()
            explored.append(curr_node.state)
            if curr_node.goal_state():
                stop = True
                if statistics:
                    stop_time = time.process_time()
                    cpu_time = stop_time - start_time
                    nodes_explored = len(explored) if self.check_visited_nodes else frontier.qsize()
                    self.running_stats = RunningStats(algorithm="bfs", duration=cpu_time, depth=curr_node.depth,
                                                      nodes=nodes_explored, cost=curr_node.cost)
                return curr_node

            successor = curr_node.successor()
            while not successor.empty():
                child_node = successor.get()
                if self.check_visited_nodes:
                    if child_node.state not in explored:
                        frontier.put(child_node)
                else:
                    frontier.put(child_node)
        return None

    def dfs(self, statistics=False):
        """Depth first search - Uses LIFO (Last-In First Out)

        Args:
            statistics (bool, optional): whether or not this algorithm should print the statistics after reaching the goal state. Defaults to False.

        Returns:
            Any: goal node or None
        """
        start_time = time.process_time() if statistics else None
        frontier = [self.start]
        explored = [self.start]
        stop = False
        while not stop:
            if len(frontier) == 0:
                return None
            curr_node = frontier.pop(0)
            explored.append(curr_node.state)
            if curr_node.goal_state():
                stop = True
                if statistics:
                    stop_time = time.process_time()
                    cpu_time = stop_time - start_time
                    nodes_explored = len(explored) if self.check_visited_nodes else len(frontier)
                    self.running_stats = RunningStats(algorithm="dfs", duration=cpu_time, depth=curr_node.depth,
                                                      nodes=nodes_explored, cost=curr_node.cost)
                return curr_node

            successor = curr_node.successor()
            while not successor.empty():
                child_node = successor.get()
                if self.check_visited_nodes:
                    if child_node.state not in explored:
                        frontier.append(child_node)
                else:
                    frontier.append(child_node)
        return None

    def dls(self, curr_node, limit):
        """Depth Limited Search. Uses LIFO queue 

        Args:
            curr_node (Node): The current node
            limit (int, optional): Search depth after which, the algorithm stops. Defaults to 50.
        """
        return self.recursive_dls(curr_node, limit)

    def recursive_dls(self, curr_node, limit):
        """Recursive Depth limited search

        Args:
            curr_node (Node): The current node
            limit (int): The limit for which the search should stop

        Returns:
            Any: Goal node or failure or 'cutoff'
        """
        if curr_node.goal_state():
            return curr_node
        elif limit == 0:
            return 'cutoff'
        else:
            cutoff_occurred = False
            successor = curr_node.successor()
            while not successor.empty():
                result = self.recursive_dls(successor.get(), limit - 1)
                if result == 'cutoff':
                    cutoff_occurred = True
                elif result is not None:
                    return result
            return 'cutoff' if cutoff_occurred else None

    def ids(self, statistics=False, limit=50):
        """Iterative Deepening search with depth_limit set to 50

        Args:
            statistics (bool, optional): Print statistics or not. Defaults to False.
            limit (int, optional): The search depth limit. Defaults to 50.

        Returns:
            Any: Goal node or None or 'cutoff'
        """
        start_time = time.process_time() if statistics else None
        for depth in range(limit):
            result = self.dls(self.start, depth)
            if result != 'cutoff':
                if statistics:
                    end_time = time.process_time()
                    cpu_time = end_time - start_time
                    self.running_stats = RunningStats(algorithm="ids", duration=cpu_time, depth=limit,
                                                      nodes=limit, cost=limit)

                return result

    def get_running_stats(self):
        """Get the running statistics for the search algorithm

        Returns: `RunningStats` the instance of the running statistics
        """
        return self.running_stats

    def statistics(self) -> None:
        """
         If statistics printing is enabled, print the statistics. Otherwise, nothing is printed.
        """
        if self.running_stats is not None:
            msg = f"\n{33 * '>'}\nStatistics for {self.running_stats.algorithm.upper()} with check for explored nodes" \
                  f" {'ENABLED' if self.check_visited_nodes else 'DISABLED'} {self.running_stats}"
            print(msg)
