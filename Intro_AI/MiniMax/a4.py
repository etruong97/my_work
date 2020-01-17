from board import Board
from player import *
import requests

instructorURL = "http://silo.cs.indiana.edu:30005"

class Game:

    def __init__(self, startBoard, player1, player2):
        self.startBoard = startBoard
        self.player1 = player1
        self.player2 = player2

    ########################################################################
    #                     Simulate a Local Game
    ########################################################################

    def simulateLocalGame(self):

        board = Board(orig=self.startBoard)

        while(True):

            # finds the move to make
            if board.turn == 0:
                move = self.player1.findMove(board)
            else:
                move = self.player2.findMove(board)

            # makes the move
            board.placeMove(move)
            board.print()

            # determines if the game is over or not
            isOver = board.isEnd()
            if isOver == -1:
                print("It is a draw!")
                break
            elif isOver == 0:
                print("Player 1 wins!")
                break
            elif isOver == 1:
                print("Player 2 wins!")
                break


    ########################################################################
    #               Simulate a Remote Game (against our server)
    #
    ########################################################################

    # Play against the instructor AI server
    
    def playAgainstInstructor(self, difficulty):

        if difficulty < 0 or difficulty > 5:
            print("Difficulty must be between 0 and 5")
            return

        board = Board(orig=self.startBoard)

        session = requests.get(instructorURL + "/startgame/" + str(difficulty)).cookies

        while (True):

            # finds the move to make
            if board.turn == 0:
                move = self.player1.findMove(board)
            else:
                r = requests.get(instructorURL + "/getresponse/" + str(board.prevMove[1]), cookies=session)
                session = r.cookies
                move = int(r.text)

            # makes the move
            board.placeMove(move)
            board.print()

            # determines if the game is over or not
            isOver = board.isEnd()
            if isOver == -1:
                print("It is a draw!")
                break
            elif isOver == 0:
                print("Your AI wins!")
                break
            elif isOver == 1:
                print("Your AI loses.")
                break


if __name__ == "__main__":

    ##########
    # How to run a local game
    ##########

    # Create a new, empty board
    b = Board()
    b2 = Board(trace=[5,3,4,6,6,0,4,6,3,3,1,4,0,1,2])
    # b2.print()
    # print(b2.board)
    # print(b2.isEnd())


    # Create player one by calling the
    # player class corresponding to the 
    # search algorithm the player uses.
    p1 = PlayerAB(5)  # 5 is the depth

    # Same for player 2
    p2 = ManualPlayer(5)

    # Create the game instance using the
    # board and players you've made.
    g = Game(b, p1, p2)

    # uncomment this line to play!
    # g.simulateLocalGame()

    # uncomment this line to play against
    # the instructor. only p1 will be used.
    # g.playAgainstInstructor(5)


