"""
Utility functions for lab1
__author__: "Bernard Longho <lobe2042@student.su.se>"
"""


class RunningStats:
    """
    A class to hold the running statistics
    """

    def __init__(self, search: str, duration: float, depth: int, nodes: int, cost: int) -> None:
        """Initialized the running statistics

        Args:
            duration (float): the time taken for the algorithm to reach a solution
            depth (int): the depth reached before a solution could be found
            nodes (int): the number of nodes generated 
            cost (int): the number of nodes in path until a solution is reached 
        """
        self.algorithm = search
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

    def save_to_file(self, filename: str) -> None:
        """Save the statistics in a file 

        Args:
            filename (str): the file for saving the statistics into 
        """
        with open(file=filename, mode="wb", encoding="utf-8") as file:
            file.write(self.__str__())
