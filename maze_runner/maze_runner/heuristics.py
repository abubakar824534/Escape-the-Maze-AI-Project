"""
heuristics.py
-------------
Heuristics for the basic maze problem (Question 6).

A heuristic is a function heuristic(state, problem) that returns an estimate
of the cost of the cheapest path from 'state' to a goal. For a MazeProblem,
'state' is a (row, col) tuple and the goal position is 'problem.goal'.
"""

import math

import util


def nullHeuristic(state, problem=None):
    """The trivial heuristic: it knows nothing, so it always says 0."""
    return 0


def manhattanHeuristic(state, problem):
    """
    Q6: the Manhattan distance from 'state' to problem.goal:
        |row1 - row2| + |col1 - col2|
    """
    "*** YOUR CODE HERE ***"
    row1, col1 = state
    row2, col2 = problem.goal
    return abs(row1 - row2) + abs(col1 - col2)
    

def euclideanHeuristic(state, problem):
    """
    Q6: the straight-line (Euclidean) distance from 'state' to problem.goal.
    """
    "*** YOUR CODE HERE ***"
    row1, col1 = state
    row2, col2 = problem.goal
    distance = (row1 - row2) ** 2 + (col1 - col2) ** 2
    return math.sqrt(distance)
  
