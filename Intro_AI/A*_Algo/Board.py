##################################
# Board Class
##################################


class Board:
    """
        This class represents the actual Board of the game

        matrix - a double sub-scripted list containing the description of the current game State
                 with 0 indicating the blank
        blankPos - a tuple containing the (row, column) position of the blank (which is denoted as 0)
    """

    # The 8-puzzle board representation
    def __init__(self, matrix):
        self.matrix = matrix
        for r, row in enumerate(matrix):
            if 0 in row:
                self.blankPos = (r, row.index(0))
                break
        else:
            raise ValueError("Invalid Matrix!")

    # A function to provide a string description of the board
    def __str__(self):
        s = ',\n'.join(str(row) for row in self.matrix)
        return s + '\n\n'

    # A function to explain how to make the board
    def __repr__(self):
        return f'Board({self.matrix})'

    # A function to checks if two Boards are equal
    def __eq__(self, other):
        if not isinstance(other, Board):
            return False
        return self.matrix == other.matrix

    # A function to create a copy of the Board object itself
    def duplicate(self):
        new_matrix = [row.copy() for row in self.matrix]
        return Board(new_matrix)

    # A function that returns a tuple containing the (row, col) position of the given element in the board
    def find_element(self, elem):
        for r, row in enumerate(self.matrix):
            for c, val in enumerate(row):
                if val == elem:
                    return (r, c)
        return None

    # A function that puts the four sliding functions together, and takes direction as input
    # move is a tuple representing (delta Y, delta X)
    def slide_blank(self, move):
        if move not in [(0, 1), (0, -1), (-1, 0), (1, 0)]:
            raise ValueError("Invalid move")
        cur_r, cur_c = self.blankPos
        delta_r, delta_c = move
        new_r, new_c = cur_r + delta_r, cur_c + delta_c
        if new_r < 0 or new_r > len(self.matrix) - 1:
            return None
        elif new_c < 0 or new_c > len(self.matrix[0]) - 1:
            return None
        else:
            new_board = self.duplicate()
            new_board.matrix[cur_r][cur_c] = new_board.matrix[new_r][new_c]
            new_board.matrix[new_r][new_c] = 0
            new_board.blankPos = (new_r, new_c)
            return new_board

    def __hash__(self):
        s = 0
        for row in self.matrix:
            for val in row:
                s *= 9  # this must be equal to w*h
                s += val
        return s
