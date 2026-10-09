"""
search.py
---------
THE MAZE RUNNER — Mini Project 1: Classical Search

This is where you implement the search algorithms (Questions 1–7).

Every algorithm receives a SearchProblem (see problems.py) and must return a
LIST OF ACTIONS that leads from the start state to a goal state, e.g.
['South', 'South', 'East']. Return [] if the start state is already a goal.

Conventions the grader relies on (please read — they matter!):

  * Use the fringe containers from util.py (Stack, Queue, PriorityQueue).
  * Calling problem.getSuccessors(state) counts as EXPANDING that state.
    Call it exactly once per expanded state, and never for a state you only
    generated.
  * Goal test when a state is POPPED from the fringe (just before you would
    expand it), not when it is pushed. (For BFS the grader also accepts
    the "early" goal test done when a state is generated.)
  * Push successors in the order getSuccessors returns them.
  * Q1, Q2, Q5, Q6, Q7 are GRAPH searches: keep a set of already-expanded
    states and never expand the same state twice.
"""

from sympy import python

import util
from util import Stack, Queue, PriorityQueue, CUTOFF
from heuristics import nullHeuristic


# ----------------------------------------------------------------------
# Q0 (worked example, not graded): always go right
# ----------------------------------------------------------------------
def alwaysRightSearch(problem):
    """
    Not a real search: the runner keeps stepping right ('East') until he
    reaches the goal. If a wall blocks the way east, he is stuck and gives up
    (returns None). It shows you how to use the problem's methods. Try it:
        python runner.py -l maze_tiny -a right     (escapes)
        python runner.py -l maze_small -a right       (walks into a wall)
    """
    state = problem.getStartState()
    actions = []
    while not problem.isGoalState(state):
        successors = problem.getSuccessors(state)   # list of (next, action, cost)
        east = [s for s in successors if s[1] == 'East']
        if not east:
            return None   # a wall straight ahead: the doors close with him inside
        nextState, action, stepCost = east[0]
        actions.append(action)
        state = nextState
    return actions


# ----------------------------------------------------------------------
# Q1: Depth-First Search
# ----------------------------------------------------------------------
def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first (graph search).

    To get started, try printing:
        print("Start:", problem.getStartState())
        print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
        print("Start's successors:", problem.getSuccessors(problem.getStartState()))

    Hint: a fringe entry can hold more than a state. Storing
    (state, actionsSoFar) is an easy way to remember how you got there.
    """
    "*** YOUR CODE HERE ***"
    stack = Stack()
    visted = set()
    start = problem.getStartState()
    stack.push((start, []))  
    
    while not stack.isEmpty():
        state, actions = stack.pop()
        
        if problem.isGoalState(state):
            return actions
        
        if state not in visted:
            visted.add(state)
            for nextState, action, cost in problem.getSuccessors(state):
                newActions = actions + [action]
                stack.push((nextState, newActions))
                
                
    return None  



# ----------------------------------------------------------------------
# Q2: Breadth-First Search
# ----------------------------------------------------------------------
def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first (graph search)."""
    "*** YOUR CODE HERE ***"
    queue = Queue()
    visited = set()
    start = problem.getStartState()
    queue.push((start, []))
    
    while not queue.isEmpty():
        state, actions = queue.pop()
        
        if problem.isGoalState(state):
            return actions
        
        if state not in visited:
            visited.add(state)
            for nextState, action, cost in problem.getSuccessors(state):
                newActions = actions + [action]
                queue.push((nextState, newActions))
                
    return None

# ----------------------------------------------------------------------
# Q3: Depth-Limited Search
# ----------------------------------------------------------------------
def depthLimitedSearch(problem, limit):
    """
    Depth-first search that never goes deeper than 'limit' actions.

    Return value:
      * a list of at most 'limit' actions that reaches a goal, or
      * CUTOFF (from util) if no goal was found but the search was stopped
        by the depth limit somewhere, so a deeper solution may exist, or
      * None if no goal was found and the limit was never reached, which
        proves there is no solution at all.

    The start state is at depth 0. A state at depth == limit may be goal
    tested but must not be expanded.

    Do NOT use a global explored set here (think about why that can make the
    search miss a solution that fits within the limit). Instead, avoid cycles
    by not revisiting a state that is already on the current path.
    """
    "*** YOUR CODE HERE ***"
    stack = Stack()
    start = problem.getStartState()
    stack.push((start, [], 0,{start}))
    cutoff = False
    
    
    while not stack.isEmpty():
        state, actions, depth, path = stack.pop()
        
        if problem.isGoalState(state):
            return actions
        
        if depth == limit:
            cutoff = True
           
        else:
            for nextState, action, cost in problem.getSuccessors(state):
                if nextState not in path:
                    newActions = actions + [action]
                    newPath = path | {nextState}
                    stack.push((nextState, newActions, depth + 1, newPath))
    if cutoff:
        return CUTOFF
    else:
        return None
    
    return None
# def depthLimitedSearch(problem, limit):
#     stack = Stack()
#     start = problem.getStartState()

#     stack.push((start, [], 0, {start}))
#     cutoff = False
#     step = 0

#     while not stack.isEmpty():
#         step += 1

#         state, actions, depth, path = stack.pop()

#         print("\n------ STEP", step, "------")
#         print("Current state:", state)
#         print("Actions:", actions)
#         print("Depth:", depth)
#         print("Path:", path)
#         print("Stack after pop:", stack.list)

#         if problem.isGoalState(state):
#             print("GOAL FOUND!")
#             return actions

#         if depth == limit:
#             cutoff = True
#             print("DEPTH LIMIT REACHED")

#         else:
#             for nextState, action, cost in problem.getSuccessors(state):

#                 print("Checking successor:", nextState)

#                 if nextState not in path:
#                     newActions = actions + [action]
#                     newPath = path | {nextState}

#                     stack.push((nextState, newActions, depth + 1, newPath))

#                     print("Pushed:", nextState)
#                     print("New actions:", newActions)
#                     print("Stack after push:", stack.list)

#                 else:
#                     print("Skipped: state already on path")

#     if cutoff:
#         print("FINAL RESULT: CUTOFF")
#         return CUTOFF
#     else:
#         print("FINAL RESULT: None")
#         return None
    
    #    cd "D:\AI Project\maze_runner\maze_runner"
    #   python runner.py -l maze_tiny -a dls -d 2 -t
        
        
# ----------------------------------------------------------------------
# Q4: Iterative Deepening Search
# ----------------------------------------------------------------------
def iterativeDeepeningSearch(problem, maxDepth=10000):
    """
    Run depthLimitedSearch with limit = 0, 1, 2, ... until it finds a
    solution. Return that solution, or None if the problem has no solution
    (or none within maxDepth).
    """
    "*** YOUR CODE HERE ***"
    limit = 0
    
    while True:
        result = depthLimitedSearch(problem, limit)
        
        if result is CUTOFF:
            limit += 1
            if limit > maxDepth:
                return None
        else:
            return result
    return None
# ----------------------------------------------------------------------
# Q5: Uniform-Cost Search
# ----------------------------------------------------------------------
def uniformCostSearch(problem):
    """Search the node of least total path cost g(n) first (graph search)."""
    "*** YOUR CODE HERE ***"
    pq = PriorityQueue()
    start = problem.getStartState()
    pq.push((start, [], 0), 0)
    visited = set()
    
    while not pq.isEmpty():
        state, actions, cost = pq.pop()
        
        if problem.isGoalState(state):
            return actions
        
        if state not in visited:
            visited.add(state)
            for nextState, action, stepCost in problem.getSuccessors(state):
                newActions = actions + [action]
                g = cost + stepCost
                pq.push((nextState, newActions, g), g)
    return None
# ----------------------------------------------------------------------
# Q6: Greedy Best-First Search
# ----------------------------------------------------------------------
def greedyBestFirstSearch(problem, heuristic=nullHeuristic):
    """
    Search the node that SEEMS closest to the goal first, i.e. the one with
    the lowest heuristic(state, problem) value (graph search).
    """
    "*** YOUR CODE HERE ***"
    pq = PriorityQueue()
    start = problem.getStartState()
    h = heuristic(start, problem)
    pq.push((start, []), h)
    
    visited = set()
    
    while not pq.isEmpty():
        state, actions = pq.pop()
        
        if problem.isGoalState(state):
            return actions
        
        if state not in visited:
            visited.add(state)
            for nextState, action, stepCost in problem.getSuccessors(state):
                newActions = actions + [action]
                h = heuristic(nextState, problem)
                pq.push((nextState, newActions), h)
                

    return None

# ----------------------------------------------------------------------
# Q7: A* Search
# ----------------------------------------------------------------------
def aStarSearch(problem, heuristic=nullHeuristic):
    """
    Search the node with the lowest f(n) = g(n) + heuristic(n) first
    (graph search).
    """
    "*** YOUR CODE HERE ***"
    pq = PriorityQueue()
    start = problem.getStartState()
    pq.push((start, [], 0), heuristic(start, problem))
    visited = set()
    
    while not pq.isEmpty():
        state, actions, cost = pq.pop()
        
        if problem.isGoalState(state):
            return actions
        
        if state not in visited:
            visited.add(state)
            for nextState, action, stepCost in problem.getSuccessors(state):
                newActions = actions + [action]
                g = cost + stepCost
                h = heuristic(nextState, problem)
                f = g + h
                pq.push((nextState, newActions, g), f)
    return None



# Abbreviations
always_right = alwaysRightSearch
dfs = depthFirstSearch
bfs = breadthFirstSearch
dls = depthLimitedSearch
ids = iterativeDeepeningSearch
ucs = uniformCostSearch
gbfs = greedyBestFirstSearch
astar = aStarSearch
