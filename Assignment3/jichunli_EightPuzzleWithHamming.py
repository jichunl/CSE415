"""jichunli_EightPuzzleWithHamming.py
This file augments EightPuzzle.py with heuristic information,
so that it can be used by an A* implementation.
The particular heuristic is hamming count, or
"the number of tiles in wrong location".
"""


from EightPuzzle import *


def h(s):

    hamming_count = 0
    goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    current_state = s.copy().b
    for i in range(3):
        for j in range(3):
            if goal_state[i][j] != 0:
                # If there is a tile
                if goal_state[i][j] != current_state[i][j]:
                    # If the goal and current state is not same
                    hamming_count += 1

    if hamming_count > 8:
        raise Exception('Hamming count should not be greater than 8')

    return hamming_count

