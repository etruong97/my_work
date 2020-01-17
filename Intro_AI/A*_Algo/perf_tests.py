#!/usr/bin/python3

import random

import a3, Board

class Case:
    def __init__(self, board, distance, manhattan, alt_goal, alt_distance, alt_manhattan):
        self.board = board
        self.distance = distance
        self.manhattan = manhattan
        self.alt_goal = alt_goal
        self.alt_distance = alt_distance
        self.alt_manhattan = alt_manhattan
    def represent(self):
        return f'{self.board} ({self.distance} moves from goal)'
    def __repr__(self):
        return f'Case(board={self.board}, distance={self.distance}, manhattan={self.manhattan}, alt_goal={self.alt_goal}, alt_distance={self.alt_distance}, alt_manhattan={self.alt_manhattan})'

def test_my_new_heuristic(cases):
    n_cases = len(cases)
    ever_less_than_zero = False
    inadmissible = False
    total_advantage_over_manhattan_main = 0
    total_advantage_over_manhattan_alt = 0

    total_distance_from_perfect_main = 0
    total_distance_from_perfect_alt = 0

    for case in cases:
        start_board = Board.Board(case.board)
        main_goal = Board.Board([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
        alt_goal  = Board.Board(case.alt_goal)

        main_heuristic_val = a3.my_new_heuristic(start_board, main_goal)
        alt_heuristic_val  = a3.my_new_heuristic(start_board, alt_goal)

        # you can write logic checking the following:
        #  - my_new_heuristic is always >= 0
        #  - my_new_heuristic is admissible
        #  - how much better or worse my_new_heuristic is than
        #    manhattan distance on the main and alt goals
        #  - how close my_new_heuristic is to perfect
        #    (always equal to the actual distance to the goal)

def test_a_star_with_manhattan(cases):
    for case in cases:
        start_board = Board.Board(case.board)
        main_goal = Board.Board([[1, 2, 3], [4, 5, 6], [7, 8, 0]])
        alt_goal  = Board.Board(case.alt_goal)

        main_goal_state = a3.a_star_solver(start_board, main_goal, a3.manhattan_distance)
        alt_goal_state = a3.a_star_solver(start_board, alt_goal, a3.manhattan_distance)

        # you can write code using time.time() around each of the above
        # calls to check how long they take, or write code checking that
        # the depth of the goal states is the same as the actual distance
        # confirmed in our test cases

if __name__ == '__main__':
    cases = [
     Case(board=[[1, 2, 3], [4, 6, 8], [0, 7, 5]], distance=6, manhattan=6, alt_goal=[[6, 2, 4], [3, 1, 7], [5, 0, 8]], alt_distance=23, alt_manhattan=15),
     Case(board=[[4, 1, 3], [2, 6, 8], [7, 0, 5]], distance=9, manhattan=9, alt_goal=[[1, 2, 3], [4, 5, 6], [0, 7, 8]], alt_distance=9, alt_manhattan=9),
     Case(board=[[7, 1, 4], [8, 0, 3], [6, 5, 2]], distance=20, manhattan=16, alt_goal=[[6, 2, 4], [3, 1, 7], [5, 0, 8]], alt_distance=23, alt_manhattan=15),
     Case(board=[[2, 0, 3], [1, 4, 6], [7, 5, 8]], distance=5, manhattan=5, alt_goal=[[1, 2, 3], [0, 5, 6], [4, 7, 8]], alt_distance=6, alt_manhattan=6),
     Case(board=[[0, 2, 3], [1, 5, 6], [4, 7, 8]], distance=4, manhattan=4, alt_goal=[[1, 2, 3], [0, 5, 6], [4, 7, 8]], alt_distance=1, alt_manhattan=1),
     Case(board=[[2, 3, 5], [0, 1, 6], [4, 8, 7]], distance=13, manhattan=9, alt_goal=[[1, 2, 3], [4, 5, 6], [0, 7, 8]], alt_distance=15, alt_manhattan=9),
     Case(board=[[1, 3, 8], [4, 2, 5], [7, 6, 0]], distance=10, manhattan=8, alt_goal=[[1, 2, 3], [4, 5, 6], [0, 7, 8]], alt_distance=10, alt_manhattan=8),
     Case(board=[[1, 3, 5], [0, 4, 2], [7, 8, 6]], distance=7, manhattan=7, alt_goal=[[1, 3, 6], [5, 2, 0], [4, 7, 8]], alt_distance=14, alt_manhattan=10),
     Case(board=[[1, 2, 0], [4, 6, 3], [7, 5, 8]], distance=4, manhattan=4, alt_goal=[[1, 2, 3], [0, 5, 6], [4, 7, 8]], alt_distance=5, alt_manhattan=5),
     Case(board=[[2, 4, 1], [0, 8, 3], [7, 6, 5]], distance=13, manhattan=11, alt_goal=[[1, 2, 3], [0, 5, 6], [4, 7, 8]], alt_distance=16, alt_manhattan=14),
     Case(board=[[5, 4, 2], [1, 0, 3], [7, 8, 6]], distance=8, manhattan=8, alt_goal=[[1, 3, 6], [5, 2, 0], [4, 7, 8]], alt_distance=15, alt_manhattan=13),
     Case(board=[[5, 2, 3], [1, 4, 0], [7, 8, 6]], distance=9, manhattan=5, alt_goal=[[1, 2, 3], [0, 5, 6], [4, 7, 8]], alt_distance=12, alt_manhattan=8),
     Case(board=[[1, 2, 3], [4, 5, 6], [7, 8, 0]], distance=0, manhattan=0, alt_goal=[[1, 3, 6], [5, 2, 0], [4, 7, 8]], alt_distance=7, alt_manhattan=7),
     Case(board=[[1, 2, 3], [8, 7, 0], [4, 6, 5]], distance=9, manhattan=9, alt_goal=[[3, 6, 8], [0, 4, 1], [2, 7, 5]], alt_distance=24, alt_manhattan=16),
     Case(board=[[1, 2, 3], [4, 8, 5], [0, 7, 6]], distance=4, manhattan=4, alt_goal=[[1, 2, 3], [0, 5, 6], [4, 7, 8]], alt_distance=7, alt_manhattan=5),
     Case(board=[[1, 3, 6], [4, 2, 0], [7, 5, 8]], distance=5, manhattan=5, alt_goal=[[1, 3, 6], [5, 2, 0], [4, 7, 8]], alt_distance=6, alt_manhattan=4),
     Case(board=[[5, 6, 0], [3, 1, 2], [4, 7, 8]], distance=14, manhattan=14, alt_goal=[[1, 3, 6], [5, 2, 0], [4, 7, 8]], alt_distance=7, alt_manhattan=7),
     Case(board=[[1, 2, 3], [4, 8, 5], [7, 0, 6]], distance=3, manhattan=3, alt_goal=[[1, 2, 3], [4, 5, 6], [0, 7, 8]], alt_distance=5, alt_manhattan=5),
     Case(board=[[1, 6, 2], [4, 5, 3], [7, 8, 0]], distance=8, manhattan=4, alt_goal=[[1, 2, 3], [4, 5, 6], [0, 7, 8]], alt_distance=8, alt_manhattan=6),
     Case(board=[[7, 4, 1], [0, 5, 3], [8, 2, 6]], distance=13, manhattan=11, alt_goal=[[3, 6, 8], [0, 4, 1], [2, 7, 5]], alt_distance=24, alt_manhattan=18),
     Case(board=[[4, 2, 3], [7, 1, 6], [8, 5, 0]], distance=12, manhattan=6, alt_goal=[[3, 6, 8], [0, 4, 1], [2, 7, 5]], alt_distance=21, alt_manhattan=17),
     Case(board=[[1, 3, 5], [8, 6, 7], [4, 0, 2]], distance=15, manhattan=13, alt_goal=[[3, 6, 8], [0, 4, 1], [2, 7, 5]], alt_distance=18, alt_manhattan=16),
     Case(board=[[5, 1, 3], [4, 2, 8], [0, 6, 7]], distance=12, manhattan=10, alt_goal=[[1, 2, 3], [0, 5, 6], [4, 7, 8]], alt_distance=9, alt_manhattan=9),
     Case(board=[[1, 2, 3], [0, 6, 8], [4, 7, 5]], distance=7, manhattan=7, alt_goal=[[1, 3, 6], [5, 2, 0], [4, 7, 8]], alt_distance=12, alt_manhattan=8),
     Case(board=[[1, 6, 5], [4, 0, 2], [7, 3, 8]], distance=12, manhattan=10, alt_goal=[[1, 2, 3], [4, 5, 6], [0, 7, 8]], alt_distance=14, alt_manhattan=10),
     Case(board=[[1, 6, 2], [4, 3, 0], [7, 5, 8]], distance=7, manhattan=7, alt_goal=[[1, 2, 3], [0, 5, 6], [4, 7, 8]], alt_distance=8, alt_manhattan=8),
     Case(board=[[0, 8, 3], [2, 4, 5], [7, 1, 6]], distance=14, manhattan=10, alt_goal=[[1, 3, 6], [5, 2, 0], [4, 7, 8]], alt_distance=21, alt_manhattan=15),
     Case(board=[[3, 5, 4], [0, 8, 1], [7, 6, 2]], distance=19, manhattan=15, alt_goal=[[1, 3, 6], [5, 2, 0], [4, 7, 8]], alt_distance=26, alt_manhattan=18),
     Case(board=[[0, 8, 3], [2, 1, 5], [4, 7, 6]], distance=10, manhattan=10, alt_goal=[[3, 6, 8], [0, 4, 1], [2, 7, 5]], alt_distance=21, alt_manhattan=11),
     Case(board=[[7, 5, 1], [0, 6, 3], [2, 4, 8]], distance=17, manhattan=13, alt_goal=[[1, 3, 6], [5, 2, 0], [4, 7, 8]], alt_distance=14, alt_manhattan=14),
     Case(board=[[0, 3, 1], [4, 5, 2], [7, 8, 6]], distance=12, manhattan=6, alt_goal=[[1, 2, 3], [0, 5, 6], [4, 7, 8]], alt_distance=15, alt_manhattan=9),
     Case(board=[[1, 0, 3], [4, 8, 5], [2, 7, 6]], distance=11, manhattan=7, alt_goal=[[1, 2, 3], [0, 5, 6], [4, 7, 8]], alt_distance=14, alt_manhattan=8),
    ]

    test_my_new_heuristic(cases)
    test_a_star_with_manhattan(cases)
