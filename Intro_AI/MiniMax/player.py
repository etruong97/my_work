import math

class BasePlayer:
    def __init__(self, maxDepth):
        self.maxDepth = maxDepth

    ##################
    #      TODO      #
    ##################
    # Assign integer scores to the three terminal states
    # P2_WIN_SCORE < TIE_SCORE < P1_WIN_SCORE
    # Access these with "self.TIE_SCORE", etc.
    P1_WIN_SCORE = 1000000000
    P2_WIN_SCORE = -1000000000
    TIE_SCORE = 0
    # Returns a heuristic for the board position
    # Good positions for 0 pieces should be positive and
    # good positions for 1 pieces should be negative
    # for all boards, P2_WIN_SCORE < heuristic(b) < P1_WIN_SCORE
    # def myHeuristic(self, board):
    #     return 0

    def myHeuristic(self, board):
        h = 1

        for i in range(board.WIDTH):
            for j in range(board.HEIGHT):
                # check vertically
                try:
                    if board.board[i][j] == board.board[i][j + 1] and \
                            board.board[i][j] == 0:
                        h = h + 5

                    if board.board[i][j] == board.board[i][j + 1] and \
                            board.board[i][j] == board.board[i][j + 2] and \
                            board.board[i][j] == 0:
                        h = h + 100

                    # if board.board[i][j] == board.board[i][j + 1] and \
                    #         board.board[i][j] == board.board[i][j + 2] and \
                    #         board.board[i][j] == board.board[i][j + 3] and \
                    #         board.board[i][j] == 0:
                    #     h = 1000000
                    #     return h
                except IndexError:
                    pass

                # check horizontally
                try:
                    if board.board[i][j] == board.board[i + 1][j] and \
                            board.board[i][j] == 0:
                        h = h + 5

                    if board.board[i][j] == board.board[i + 1][j] and \
                            board.board[i][j] == board.board[i + 2][j] and \
                            board.board[i][j] == 0:
                        h = h + 100

                    # if board.board[i][j] == board.board[i + 1][j] and \
                    #         board.board[i][j] == board.board[i + 2][j] and \
                    #         board.board[i][j] == board.board[i + 3][j] and \
                    #         board.board[i][j] == 0:
                    #     h = 1000000
                    #     return h
                except IndexError:
                    pass

                # check upward diagonal
                try:
                    if board.board[i][j] == board.board[i + 1][j + 1] and \
                            board.board[i][j] == 0:
                        h = h + 5

                    if board.board[i][j] == board.board[i + 1][j + 1] and \
                            board.board[i][j] == board.board[i + 2][j + 2] and \
                            board.board[i][j] == 0:
                        h = h + 100

                    # if board.board[i][j] == board.board[i + 1][j + 1] and \
                    #         board.board[i][j] == board.board[i + 2][j + 2] and \
                    #         board.board[i][j] == board.board[i + 3][j + 3] and \
                    #         board.board[i][j] == 0:
                    #     h = 1000000
                    #     return h
                except IndexError:
                    pass

                # check downward diagonal
                try:
                    if board.board[i][j] == board.board[i + 1][j - 1] and \
                            board.board[i][j] == 0 and \
                            j > 0:
                        h = h + 5

                    if board.board[i][j] == board.board[i + 1][j - 1] and \
                            board.board[i][j] == board.board[i + 2][j - 2] and \
                            board.board[i][j] == 0 and \
                            j > 0:
                        h = h + 100

                    # if board.board[i][j] == board.board[i + 1][j - 1] and \
                    #         board.board[i][j] == board.board[i + 2][j - 2] and \
                    #         board.board[i][j] == board.board[i + 3][j - 3] and \
                    #         board.board[i][j] == 0 and \
                    #         j > 0:
                    #     h = 1000000
                    #     return h
                except IndexError:
                    pass

                ###########################################################

                try:
                    if board.board[i][j] == board.board[i][j + 1] and \
                            board.board[i][j] == 1:
                        h = h - 5

                    if board.board[i][j] == board.board[i][j + 1] and \
                            board.board[i][j] == board.board[i][j + 2] and \
                            board.board[i][j] == 1:
                        h = h - 100

                    # if board.board[i][j] == board.board[i][j + 1] and \
                    #         board.board[i][j] == board.board[i][j + 2] and \
                    #         board.board[i][j] == board.board[i][j + 3] and \
                    #         board.board[i][j] == 1:
                    #     h = -1000000
                    #     return h
                except IndexError:
                    pass

                # check horizontally
                try:
                    if board.board[i][j] == board.board[i + 1][j] and \
                            board.board[i][j] == 1:
                        h = h - 5

                    if board.board[i][j] == board.board[i + 1][j] and \
                            board.board[i][j] == board.board[i + 2][j] and \
                            board.board[i][j] == 1:
                        h = h - 100

                    # if board.board[i][j] == board.board[i + 1][j] and \
                    #         board.board[i][j] == board.board[i + 2][j] and \
                    #         board.board[i][j] == board.board[i + 3][j] and \
                    #         board.board[i][j] == 1:
                    #     h = -1000000
                    #     return h
                except IndexError:
                    pass

                # check upward diagonal
                try:
                    if board.board[i][j] == board.board[i + 1][j + 1] and \
                            board.board[i][j] == 1:
                        h = h - 5

                    if board.board[i][j] == board.board[i + 1][j + 1] and \
                            board.board[i][j] == board.board[i + 2][j + 2] and \
                            board.board[i][j] == 1:
                        h = h - 100

                    # if board.board[i][j] == board.board[i + 1][j + 1] and \
                    #         board.board[i][j] == board.board[i + 2][j + 2] and \
                    #         board.board[i][j] == board.board[i + 3][j + 3] and \
                    #         board.board[i][j] == 1:
                    #     h = -1000000
                    #     return h
                except IndexError:
                    pass

                # check downward diagonal
                try:
                    if board.board[i][j] == board.board[i + 1][j - 1] and \
                            board.board[i][j] == 1 and \
                            j > 0:
                        h = h - 5

                    if board.board[i][j] == board.board[i + 1][j - 1] and \
                            board.board[i][j] == board.board[i + 2][j - 2] and \
                            board.board[i][j] == 1 and \
                            j > 0:
                        h = h - 100

                    # if board.board[i][j] == board.board[i + 1][j - 1] and \
                    #         board.board[i][j] == board.board[i + 2][j - 2] and \
                    #         board.board[i][j] == board.board[i + 3][j - 3] and \
                    #         board.board[i][j] == 1 and \
                    #         j > 0:
                    #     h = -1000000
                    #     return h
                except IndexError:
                    pass

        if board.isFull():
            return 0

        return h


class ManualPlayer(BasePlayer):
    def __init__(self, maxDepth=None):
        BasePlayer.__init__(self, maxDepth)

    def findMove(self, board):
        opts = " "
        for c in range(board.WIDTH):
            opts += " "+(str(c+1) if len(board.board[c]) < board.HEIGHT else ' ')+"  "
        print(opts)

        while True:
            col = input("Place a "+('O' if board.turn == 0 else 'X')+" in column: ")
            try: col = int(col) - 1
            except ValueError: continue
            if col >= 0 and col < board.WIDTH and len(board.board[col]) < board.HEIGHT:
                return col


class PlayerMM(BasePlayer):
    ##################
    #      TODO      #
    ##################
    # performs minimax on board with depth.
    # returns the best move and best score as a tuple
    def minimax(self, board, depth):
        if board.isEnd() == -1:
            return None, self.TIE_SCORE
        if board.isEnd() == 0:
            return None, self.P1_WIN_SCORE
        if board.isEnd() == 1:
            return None, self.P2_WIN_SCORE
        if depth == 0:
            return None, self.myHeuristic(board)

        max_move = None
        min_move = None

        best_val_max = -math.inf
        best_val_min = math.inf

        for i in board.getAllValidMoves():
            child = board.getChild(i)
            v = self.minimax(child, depth - 1)[1]
            if board.turn == 0:
                if v >= best_val_max:
                    best_val_max = v
                    max_move = i
            else:
                if v <= best_val_min:
                    best_val_min = v
                    min_move = i

        if board.turn == 0:
            return max_move, best_val_max
        else:
            return min_move, best_val_min


    def findMove(self, board):
        move, score = self.minimax(board, self.maxDepth)
        return move


class PlayerAB(BasePlayer):
    ##################
    #      TODO      #
    ##################
    # performs minimax with alpha-beta pruning on board with depth.
    # alpha represents the score of max's current strategy
    # beta  represents the score of min's current strategy
    # in a cutoff situation, return the score that resulted in the cutoff
    # returns the best move and best score as a tuple
    # def alphaBeta(self, alpha, beta, board, depth):
    #     if depth == 0:
    #         return None, self.myHeuristic(board)
    #     if board.isEnd() == -1:
    #         return None, self.TIE_SCORE
    #     if board.isEnd() == 0:
    #         return None, self.P1_WIN_SCORE
    #     if board.isEnd() == 1:
    #         return None, self.P2_WIN_SCORE
    #
    #     max_move = None
    #     min_move = None
    #     best_val = -math.inf
    #
    #     if board.turn == 0:
    #         best_val = -math.inf
    #     else:
    #         best_val = math.inf
    #
    #     for i in board.getAllValidMoves():
    #         child = board.getChild(i)
    #         v = self.alphaBeta(alpha, beta, child, depth - 1)[1]
    #         if board.turn == 0:
    #             if v >= best_val:
    #                 best_val = v
    #                 max_move = i
    #                 alpha = max(alpha, best_val)
    #                 if alpha >= beta:
    #                     break
    #
    #         elif board.turn == 1:
    #             if v <= best_val:
    #                 best_val = v
    #                 min_move = i
    #                 beta = min(beta, best_val)
    #                 if alpha >= beta:
    #                     break
    #
    #     if board.turn == 0:
    #         return max_move, best_val
    #     else:
    #         return min_move, best_val

    def alphaBeta(self, alpha, beta, board, depth):
        if board.isEnd() == -1:
            return None, self.TIE_SCORE
        if board.isEnd() == 0:
            return None, self.P1_WIN_SCORE
        if board.isEnd() == 1:
            return None, self.P2_WIN_SCORE
        if depth == 0:
            return None, self.myHeuristic(board)

        max_move = None
        min_move = None
        best_val_max = -math.inf
        best_val_min = math.inf

        for i in board.getAllValidMoves():
            child = board.getChild(i)
            v = self.alphaBeta(alpha, beta, child, depth - 1)[1]
            if board.turn == 0:
                if v > best_val_max:
                    best_val_max = v
                    max_move = i
                    alpha = max(alpha, best_val_max)
                    if alpha >= beta:
                        return None, alpha

            else:
                if v < best_val_min:
                    best_val_min = v
                    min_move = i
                    beta = min(beta, best_val_min)
                    if alpha >= beta:
                        return None, beta

        if board.turn == 0:
            return max_move, best_val_max
        else:
            return min_move, best_val_min

    def findMove(self, board):
        move, score = self.alphaBeta(-math.inf, math.inf, board, self.maxDepth)
        return move


class PlayerDP(PlayerAB):
    ''' A version of PlayerAB that implements dynamic programming
        to cache values for its heuristic function, improving performance. '''
    def __init__(self, maxDepth):
        PlayerAB.__init__(self, maxDepth)

        self.resolved = {}

    ##################
    #      TODO      #
    ##################
    # if a saved heuristic value exists in self.resolved for board.state, returns that value
    # otherwise, uses BasePlayer.myHeuristic to get a heuristic value and saves it under board.state
    def myHeuristic(self, board):
        # raise NotImplementedError
        if board.state in self.resolved:
            return self.resolved[board.state]
        else:
            h = BasePlayer.myHeuristic(self, board)
            self.resolved.update({board.state: h})
            return h


#######################################################
###########Example Subclass for Testing
#######################################################

# This will inherit your findMove from above, but will override the heuristic function with
# a new one; you can swap out the type of player by changing X in "class TestPlayer(X):"
class TestPlayer(BasePlayer):
    # define your new heuristic here
    def myHeurisitic(self):
        pass





