#!/usr/bin/python3

# B351/Q351 Spring 2019
# Professor Saúl Blanco
# Do not share these assignments or their solutions outside of this class.

###################################
#                                 #
# Assignment 3: Search Algorithms #
#                                 #
###################################
import time
import math
import State
import Board
import heapq

STOP = -1
CONTINUE = 0


#################################
# Problem 1 - Fringe Expansion
#################################
# Objective:
# 1) Write a function that adds the possible states that we can get to
#    from the current state to the end of the fringe.
#
# Notes:
# (1) This function should not return or yield anything but just update the contents of the fringe
# (2) board.slide_blank is error-safe. It will return None if it is impossible to slide the blank

def fringe_expansion(current_state, fringe):
    moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    for m in moves:
        if current_state.board.slide_blank(m) is None:
            continue
        else:
            fringe.append(State.State(current_state.board.slide_blank(m),
                          current_state,
                          current_state.depth + 1))


#################################
# Problem 2 - BFS
#################################
# Objectives:
# (1) Write a function that implements a single iteration of the BFS algorithm
#     by considering the first state from the fringe.
#     (Returns STOP if the fringe is empty.)
#     See the project documentation for more details.

def bfs(fringe, max_depth, goal_board):
    if len(fringe) == 0:
        return STOP
    current_state = fringe.pop(0)
    if current_state.depth > max_depth:
        return CONTINUE
    if current_state.board.__eq__(goal_board):
        return current_state
    fringe_expansion(fringe[0], fringe)
    return CONTINUE


def uninformed_solver(start_board, max_depth, goal_board):
    """
        Looping function which calls bfs until it finds a solution (a State object) or
        until STOP has been returned. Does not consider States below max_depth.
        If the goal is reached, this function should return the Goal State,
        which includes a path to the goal. Otherwise, returns None.
    """
    fringe = [State.State(start_board, None, None, 0)]
    found = CONTINUE
    while found == CONTINUE:
        found = bfs(fringe, max_depth, goal_board)
    if isinstance(found, State.State):
        # Found goal!
        return found
    # Max depth reached...
    return None


####################################
# Problem 3 - UCS f-value Function
####################################
# Objectives:
# (1) Write a function that takes a board and depth and returns the f-value
#     (priority) that board should have in a uniform-cost search scenario.

def ucs_f_value_function(board, depth):
    return depth


###########################################
# Problem 4 - A* f-value Function Factory
###########################################
# Objectives:
# (1) Given a heuristic function and a goal board, returns a f-value FUNCTION
#     (like ucs_f_function) that evaluates boards and depths as in the A* algorithm.
#
# Notes:
# (1) It may be helpful to consult your solution for a1.compose here.

def a_star_f_value_function_factory(heuristic, goal_board):
    return lambda board, depth: heuristic(board, goal_board) + depth


# Here is an example heuristic function.
def manhattan_distance(current_board, goal_board):
    total = 0
    goal_matrix = goal_board.matrix
    for goal_r in range(0, 3):
        for goal_c in range(0, 3):
            val = goal_matrix[goal_r][goal_c]
            if val == 0:
                continue
            current_r, current_c = current_board.find_element(val)
            total += abs(goal_r - current_r) + abs(goal_c - current_c)
    return total

#################################
# Problem 5 - Your Own Heuristic
#################################
# Objectives:
# (1) Write a function that takes current_board and goal_board as arguments and
#     returns an estimate of how many moves it will take to reach the goal board.
#     Your heuristic must be admissible (never overestimate cost to goal), but
#     it does not have to be consistent (never overestimate step costs).
#
# Notes:
# (1) This heuristic should be admissible, but greater than (closer to the real
#     value than) the manhattan distance heuristic on average. That makes it a
#     better heuristic.


def my_new_heuristic(current_board, goal_board):
    total = 0
    goal_matrix = goal_board.matrix
    for goal_r in range(0, 3):
        for goal_c in range(0, 3):
            val = goal_matrix[goal_r][goal_c]
            if val == 0:
                continue
            current_r, current_c = current_board.find_element(val)
            total += math.sqrt(((goal_r - current_r) ** 2) + ((goal_c - current_c) ** 2))
    return total

#################################
# Problem 6 - Informed Expansion
#################################
# Objectives:
# (1) Write a function that expands the fringe using the f-value function
#     provided. Note that States automatically sort by their f-values.
#
# Notes:
# (1) This function should update the contents of the fringe using heapq.


def informed_expansion(current_state, fringe, f_function):
    moves = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    for m in moves:
        if current_state.board.slide_blank(m) is None:
            continue
        else:
            child = current_state.board.slide_blank(m)
            heapq.heappush(fringe,
                           State.State(child,
                                       current_state,
                                       current_state.depth + 1,
                                       f_value=f_function(child, current_state.depth + 1)))


#################################
# Problem 7 - Informed Search
#################################
# Objectives:
# (1) Write a function that implements a single iteration of the
#     A*/UCS algorithm by considering the top-priority state from the fringe.
#     (Returns STOP if the fringe is empty.)
#     See the project documentation for more details.


def informed_search(fringe, goal_board, f_function, explored):
    if len(fringe) == 0:
        return STOP

    top_state = heapq.heappop(fringe)
    if top_state.board in explored and top_state.f_value >= explored[top_state.board]:
        return CONTINUE
    else:
        explored.update({top_state.board: top_state.f_value})
    if top_state.board.__eq__(goal_board):
        return top_state
    else:
        informed_expansion(top_state, fringe, f_function)
        return CONTINUE


def informed_solver(start_board, goal_board, f_function):
    """
        Looping function which calls informed_search until it finds a solution
        (a State object) or until STOP has been returned.
        If the goal is reached, this function should return the Goal State,
        which includes a path to the goal. Otherwise, returns None.
    """
    fringe = [State.State(start_board, None, 0, f_function(start_board, 0))]
    explored = {}
    found = CONTINUE
    while found == CONTINUE:
        found = informed_search(fringe, goal_board, f_function, explored)
    if isinstance(found, State.State):
        return found
    return None


def ucs_solver(start_board, goal_board):
    return informed_solver(start_board, goal_board, ucs_f_value_function)


def a_star_solver(start_board, goal_board, heuristic):
    f_function = a_star_f_value_function_factory(heuristic, goal_board)
    return informed_solver(start_board, goal_board, f_function)

#################################
# Bonus Problem - IDS (10pts)
#################################
# Implement IDS in any way you choose. You will probably want to write multiple
# helper functions; be sure to document these appropriately.
#
# ids should take a start board and goal board and then perform multiple
# depth-first searches, with the maximum depth increasing from 0 all the way to
# final depth.
#
# If there is a solution within final_depth moves, ids should return it as a Board object.
# Otherwise, return None.


def ids(start_board, goal_board, final_depth):
    return

###########################
# Main method for testing #
###########################


def main():
    goal_board = Board.Board([[1, 2, 3],
                              [4, 5, 6],
                              [7, 8, 0]])

    simple_board = Board.Board([[1, 2, 0],
                              [4, 5, 3],
                              [7, 8, 6]])

    # Simple test case for fringe_expansion
    fringe1 = []
    node1 = State.State(simple_board, None, 0, 0)
    fringe_expansion(node1, fringe1)
    assert State.State(simple_board.slide_blank((-1, 0)), node1, 0, 0) not in fringe1
    assert State.State(simple_board.slide_blank((0, -1)), node1, 0, 1) in fringe1

    # Simple test case for BFS
    fringe1 = []
    node1 = State.State(simple_board, None, 0, 0)
    fringe_expansion(node1, fringe1)
    assert bfs(fringe1, 3, goal_board) == CONTINUE
    fringe1[0] = State.State(goal_board, node1, 0, 0)
    assert type(bfs(fringe1, 3, goal_board)) is State.State

    # Simple test case for ucs_f_value_function
    node1 = State.State(simple_board, None, 0, 0)
    assert ucs_f_value_function(node1.board, 0) == 0

    # Simple test case for a_star_f_value_function
    # -> This checks that the return type is correct
    assert hasattr(a_star_f_value_function_factory(None, goal_board), '__call__')

    # This section is for you to create tests for your own heuristic

    # Simple test for Informed Expansion
    node1 = State.State(simple_board, None, 0, 0)
    fringe1 = []
    informed_expansion(node1, fringe1, ucs_f_value_function)
    assert State.State(simple_board.slide_blank((-1, 0)), node1, 0, 0) not in fringe1
    assert State.State(simple_board.slide_blank((0, -1)), node1, 0, 1) in fringe1

    # Simple test for Informed Search
    fringe1 = []
    explored = {}
    node1 = State.State(simple_board, None, 0, 0)
    fringe_expansion(node1, fringe1)
    assert informed_search(fringe1, goal_board, ucs_f_value_function, explored) == CONTINUE
    fringe1[0] = State.State(goal_board, node1, 0, 0)
    assert type(informed_search(fringe1, goal_board, ucs_f_value_function, explored)) is State.State

    # Simple test for IDS
    # node1 = State.State(simple_board, None, 0, 0)
    # assert ids(node1.board, goal_board, 1) is None
    # assert type(ids(node1.board, goal_board, 2)) is Board.Board



if __name__ == "__main__":
    main()
