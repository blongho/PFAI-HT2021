"""
Utility functions for lab1
__author__: "Bernard Longho <lobe2042@student.su.se>"
"""


class RunningStats:
    """
    A class to hold the running statistics
    """

    def __init__(self, algorithm: str, duration: float, depth: int, nodes: int, cost: int) -> None:
        """Initialized the running statistics

        Args:
            duration (float): the time taken for the algorithm to reach a solution
            depth (int): the depth reached before a solution could be found
            nodes (int): the number of nodes generated 
            cost (int): the number of nodes in path until a solution is reached 
        """
        self.algorithm = algorithm
        self.duration = duration
        self.depth = depth
        self.nodes = nodes
        self.cost = cost
        self.branching_factor = pow(self.nodes, 1 / depth)

    def __str__(self) -> str:
        """A string representation of the running stats. This allows the object to be printed like

        running_stats = RunningStats(value, value....)

        print(running_stats)

        Returns:
            str: string representation of this class
        """
        return "\n--------------------------------\n" \
               f"Elapsed time (s): {self.duration}\n" \
               f"Solution found at depth: {self.depth}\n" \
               f"Number of nodes explored: {self.nodes}\n" \
               f"Cost of solution: {self.cost}\n" \
               f"Estimated effective branching factor: {self.branching_factor}\n" \
               "--------------------------------\n"

    def save_to_file(self, filename: str, msg:str) -> None:
        """Save the statistics in a file 

        Args:
            filename (str): the file for saving the statistics into 
            msg (str): Another message to add to file
        """
        with open(file=filename, mode="a") as file:
            file.write(msg)
            file.write(self.__str__())


def get_configuration(args: list) -> dict():
    arguments = {}
    for item in args:
        if item.startswith("timer"):
            timing_enabled = item.split("=")[1]
            arguments["enable_timing"] = timing_enabled
        if item.startswith("algo"):
            algo = item.split("=")[1]
            arguments["algo"] = algo
        if item.startswith("save_to_file"):
            saving_to_file = item.split("=")[1]
            arguments["save_to_file"] = saving_to_file
        if item.startswith("statistics"):
            statistics = item.split("=")[1]
            arguments["statistics"] = statistics
        if item.startswith("check_visited_nodes"):
            visited_check = item.split("=")[1]
            arguments["check_visited_nodes"] = visited_check
        if item.startswith("pretty_print"):
            pretty_print = item.split("=")[1]
            arguments["pretty_print"] = pretty_print
        
    return arguments
