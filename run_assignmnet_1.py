"""
Define problem and start execution of search problems

Author: Tony Lindgren, Longho Bernard Che (lobe2042), Mba Godwin(gomb0114)
"""
from missionaries_and_cannibals import MissionariesAndCannibals
from node_and_search import SearchAlgorithm
from utils import save_content_to_file as WriteToFile

filename = "Assignment1-Report+Longho_Bernard_Che_and_Mba_Godwin.md"
init_state = [[0, 0], 'r', [3, 3]]
goal_state = [[3, 3], 'l', [0, 0]]


def run_mm_cc(algorithm="bfs", print_stats=True, verbose_print=True, check_visited_nodes=False, save_to_file=True):
    """Run the Missionaries and Cannibals solver

    Args:
        algorithm (str, optional): the algorithm used for solving the problem. Defaults to "bfs".
        print_stats (bool, optional): whether or not the running statistics will be printed. Defaults to True.
        verbose_print (bool, optional): whether the action and path shall be printed. Defaults to True.
        check_visited_nodes (bool, optional): whether or not already visited nodes is checked before adding a node to the frontier. Defaults to False.
        save_to_file (bool, optional): whether the results shall be saved to file. Defaults to True.
    """
    message = f"\nRunning {algorithm.upper()} with the following configuration:" \
              f" {' check for explored nodes.' if check_visited_nodes else ' not checking explored nodes.'}  "
    print(message)

    mc = MissionariesAndCannibals(init_state, goal_state)

    sa = SearchAlgorithm(mc, check_visited_nodes=check_visited_nodes)
    # ============= BFS ==================
    if algorithm.lower() == "bfs":
        print("BFS")
        print('Start state: ')

        mc.pretty_print()
        goal_node = sa.bfs(statistics=print_stats)
        goal_node.pretty_print_solution(verbose=verbose_print)

        print('goal state: ')

        goal_node.state.pretty_print()

        if print_stats:
            sa.statistics()
    else:
        print("DFS")
        print('Start state: ')
        mc.pretty_print()
        goal_node = sa.dfs(statistics=print_stats)
        goal_node.pretty_print_solution(verbose=verbose_print)

        print('goal state: ')

        goal_node.state.pretty_print()

        if print_stats:
            sa.statistics()

    if save_to_file:
        WriteToFile(filename=filename, msg=message)
        WriteToFile(filename=filename, msg=str(sa.get_running_stats()))


def main():
    run_mm_cc(algorithm="bfs", print_stats=True, verbose_print=True, check_visited_nodes=True)
    run_mm_cc(algorithm="dfs", print_stats=True, verbose_print=True, check_visited_nodes=True)

    # Not checking for explored nodes
    run_mm_cc(algorithm="bfs", print_stats=True, verbose_print=True, check_visited_nodes=False)
    run_mm_cc(algorithm="dfs", print_stats=True, verbose_print=True, check_visited_nodes=False)


if __name__ == "__main__":
    main()
