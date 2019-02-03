"""jichunli_EightPuzzleWithManhattan.py
This file augments EightPuzzle.py with heuristic information,
so that it can be used by an A* implementation.
The particular heuristic is Manhattan Distance.
"""

from EightPuzzle import *


def h(s):

    manhattan_distance = 0
    goal_state = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    current_state = s.copy().b
    current_location = {}

    for row in range(3):
        for col in range(3):
            current_location[current_state[row][col]] = [row, col]

    for row in range(3):
        for col in range(3):
            if goal_state[row][col] != 0:
                # If there is a tile
                goal_location = current_location[goal_state[row][col]]
                manhattan_distance += abs(row - goal_location[0])
                manhattan_distance += abs(col - goal_location[1])
    return manhattan_distance

