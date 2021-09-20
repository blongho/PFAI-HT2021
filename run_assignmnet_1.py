'''
Define problem and start execution of search problems

Author: Tony Lindgren
'''
import sys

from missionaries_and_cannibals import MissionariesAndCannibals
from node_and_search import SearchAlgorithm
from utils import get_configuration

init_state = [[0, 0], 'r', [3, 3]]
goal_state = [[3, 3], 'l', [0, 0]]


def main():
    config = get_configuration(sys.argv)

    mc = MissionariesAndCannibals(init_state, goal_state)

    sa = SearchAlgorithm(mc, check_visited_nodes=True)

    print('Start state: ')

    mc.pretty_print()

    algo = config.get('algo')
    if algo == "bfs":
        goal_node = sa.bfs(statistics=True)
    else:
        goal_node = sa.dfs(statistics=True)

    goal_node.pretty_print_solution(verbose=True)

    print('goal state: ')

    goal_node.state.pretty_print()

    sa.statistics()


if __name__ == "__main__":
    main()
