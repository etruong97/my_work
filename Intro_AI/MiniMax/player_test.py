from board import Board
from player import *

def player_check(board, expected, board_name, status):
    totalpassedtest = 0

    print()
    print("+" + "++++" * width*2)
    print()
    
    try:
        print("MiniMax Test of {} turn {}: ".format(board_name, status), end = "")
        if mmPlayer.findMove(board) == expected:
            print("Passed")
            totalpassedtest +=  1
        else:
            print("Failed")
            print("Expect: {}, Return: {}".format(expected, mmPlayer.findMove(board)), end = "")
            board.print() # 610
    except NotImplementedError:
        print('minimax not implemented.')

    try:
        print("\nAlphaBeta Test of {} turn {}: ".format(board_name, status), end = "")
        if abPlayer.findMove(board) == expected:
            print("Passed")
            totalpassedtest +=  1
        else:
            print("Failed")
            print("Expect: {}, Return: {}".format(expected, abPlayer.findMove(board)), end = "")
            board.print() # 610
    except NotImplementedError:
        print('alphaBeta not implemented.')

    try:
        print("\nD-Programming Test of {} turn {}: ".format(board_name, status), end = "")
        if dpPlayer.findMove(board) == expected:
            print("Passed")
            totalpassedtest +=  1
        else:
            print("Failed")
            print("Expect: {}, Return: {}".format(expected, dpPlayer.findMove(board)), end = "")
            board.print() # 610
    except NotImplementedError:
        print('alphaBeta not implemented.')

    return totalpassedtest



def isEnd_check(board, expected, board_name):
    try:
        print()
        print("+" + "++++" * width*2)
        print()
        print("isEnd() Test of {}: ".format(board_name), end = "")
        if board.isEnd() == expected:
            print("Passed")
            return 1
        else:
            print("Failed")
            print("Expect: {}, Return: {}".format(expected, board.isEnd()))
            test_Board_THREE.print() # 610
            return 0 
    except NotImplementedError:
        print('isEnd() not implemented.')
        return 0 


if __name__ == '__main__':
    ####################################################
    #    Test for findMove() (minimax and alphaBeta)   #
    ####################################################

    '''
    These tests only handle the terminal cases. If you want to check a case of certain
    move, please write your own tests.
    '''

    # if you modified the HEIGHT and WIDTH in board class, be sure to modify this two
    height = 6
    width = 7

    maxDepth = 5

    total_test = 28
    passed_test = 0

    # Four cases of winning; this does not cover every possible case, so you still
    # may get point deductions in autograder even though you pass all the tests here
    test_Board_ONE = Board()
    test_Board_TWO = Board()
    test_Board_THREE = Board()
    test_Board_FOUR = Board()

    # construction of each board
    test_Board_TWO.placeMove(width - 1)
    test_Board_FOUR.placeMove(0)

    for i in range(3):
        for j in range(i):
            test_Board_THREE.placeMove(j)
            test_Board_FOUR.placeMove(width - j - 1)

    for i in range(2):
        test_Board_ONE.placeMove(1)
        test_Board_ONE.placeMove(3)

        test_Board_TWO.placeMove(i)
        test_Board_TWO.placeMove(i)

        test_Board_THREE.placeMove(i)
        test_Board_THREE.placeMove(width-1)

        test_Board_FOUR.placeMove(width - i - 1)
        test_Board_FOUR.placeMove(1)

    test_Board_ONE.placeMove(1)

    test_Board_TWO.placeMove(2)

    test_Board_THREE.placeMove(2)
    test_Board_THREE.placeMove(0)
    test_Board_THREE.placeMove(width - 1)
    test_Board_THREE.placeMove(1)
    test_Board_THREE.placeMove(width - 1)
    test_Board_THREE.placeMove(2)

    test_Board_FOUR.placeMove(width - 3)
    test_Board_FOUR.placeMove(width - 1)
    test_Board_FOUR.placeMove(0)
    test_Board_FOUR.placeMove(width - 2)
    test_Board_FOUR.placeMove(1)
    test_Board_FOUR.placeMove(width - 3)
    
    mmPlayer = PlayerMM(maxDepth)
    abPlayer = PlayerAB(maxDepth)
    dpPlayer = PlayerDP(maxDepth)

    # test of test_Board_ONE Player X Defense
    passed_test += player_check(test_Board_ONE, 1, "Board ONE", "X")

    # test of test_Board_ONE Player O attack
    test_Board_ONE.placeMove(0)
    passed_test += player_check(test_Board_ONE, 1, "Board ONE", "O")

    # test of test_Board_TWO Player O Defense
    passed_test += player_check(test_Board_TWO, 3, "Board TWO", "O")

    # test of test_Board_TWO Player X attack
    test_Board_TWO.placeMove(4)
    passed_test += player_check(test_Board_TWO, 3, "Board TWO", "X")

    # test of test_Board_THREE Player X Defense
    passed_test += player_check(test_Board_THREE, 3, "Board THREE", "X")
    
    # test of test_Board_THREE Player O attack
    test_Board_THREE.placeMove(0)
    passed_test += player_check(test_Board_THREE, 3, "Board THREE", "O")
    
    # test of test_Board_FOUR Player O Defense
    passed_test += player_check(test_Board_FOUR, width - 4, "Board FOUR", "O")
    
    # test of test_Board_FOUR Player X attack
    test_Board_FOUR.placeMove(0)
    passed_test += player_check(test_Board_FOUR, width - 4, "Board FOUR", "X")


    
    #############################
    #      Test for isEnd()     #
    #############################
    
    # return case of isEnd()
    # be sure to update this if you have different representation of each player's win. 
    playerZeroWin = 0
    playerOneWin = 1

    test_Board_ONE.placeMove(1)
    test_Board_TWO.placeMove(3)
    test_Board_THREE.placeMove(3)
    test_Board_FOUR.placeMove(width - 4)

    passed_test += isEnd_check(test_Board_ONE, playerZeroWin, "Board ONE")
    passed_test += isEnd_check(test_Board_TWO, playerOneWin, "Board TWO")
    passed_test += isEnd_check(test_Board_THREE, playerZeroWin, "Board THREE")
    passed_test += isEnd_check(test_Board_FOUR, playerOneWin, "Board FOUR")


    print("\n\n", "Total Tests: ", total_test)
    print("Passed Tests: ", passed_test)
    


    ##############################
    #  To write your own TESTS!!! #
    ##############################

    # TESTS you should make by yourself:
    # 1. Check for non-winner board.
    #    You should have a case for handling boards which have no winner (every empty space is filled, but no winner).
    #
    # 2. Check for Tie in minimax and alphabeta functions:
    #    You should have a case to break tie if there are two moves that is equally good
    #
    # 3. Check for moves in non-terminal state
    #    The given test for minimax and alphabeta only checks if the functions can handle cases before checkmate
    #    You should have tests to check if the functions also make smart moves for normal case
