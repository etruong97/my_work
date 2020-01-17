import csv
import itertools

class Board():

    ##########################################
    ####   Constructor
    ##########################################
    def __init__(self, filename):

        # initialize all of the variables
        self.n2 = 0  # length of entire edge
        self.n = 0  # box size
        self.spaces = 0  # total spaces
        self.board = None  # dictionary of {(r,c): int}
        self.valuesInRows = None
        self.valuesInCols = None
        self.valuesInBoxes = None
        self.unsolved = None  # set of coordinates with no value

        # load the file and initialize the in-memory board with the data
        self.loadSudoku(filename)


    #loads the sudoku board from the given file
    def loadSudoku(self, filename):

        with open(filename) as csvFile:
            self.n = -1
            reader = csv.reader(csvFile)
            for row in reader:

                #Assign the n value and construct the approriately sized dependent data
                if self.n == -1:
                    self.n = int(len(row) ** (1/2))
                    if not self.n ** 2 == len(row):
                        raise Exception('Each row must have n^2 values! (See row 0)')
                    else:
                        self.n2 = len(row)
                        self.spaces = self.n ** 4
                        self.board = {}
                        self.valuesInRows = [set() for _ in range(self.n2)]
                        self.valuesInCols = [set() for _ in range(self.n2)]
                        self.valuesInBoxes = [set() for _ in range(self.n2)]
                        self.unsolved = set(itertools.product(range(self.n2), range(self.n2)))

                #check if each row has the correct number of values
                else:
                    if len(row) != self.n2:
                        raise Exception('Each row must have the same number of values. (See row ' + str(reader.line_num - 1) + ')')

                #add each value to the correct place in the board; record that the row, col, and box contains value
                for index, item in enumerate(row):
                    if not item == '':
                        self.board[(reader.line_num-1, index)] = int(item)
                        self.valuesInRows[reader.line_num-1].add(int(item))
                        self.valuesInCols[index].add(int(item))
                        self.valuesInBoxes[self.spaceToBox(reader.line_num-1, index)].add(int(item))
                        self.unsolved.remove((reader.line_num-1, index))


    ##########################################
    ####   Utility Functions
    ##########################################

    #converts a given row and column to its inner box number
    def spaceToBox(self, row, col):
        return self.n * (row // self.n) + col // self.n

    #prints out a command line representation of the board
    def print(self):
        for r in range(self.n2):
            #add row divider
            if r % self.n == 0 and not r == 0:
                if self.n2 > 9:
                    print("  " + "----" * self.n2)
                else:
                    print("  " + "---" * self.n2)

            row = ""

            for c in range(self.n2):

                if (r,c) in self.board:
                    val = self.board[(r,c)]
                else:
                    val = None

                #add column divider
                if c % self.n == 0 and not c == 0:
                    row += " | "
                else:
                    row += "  "

                #add value placeholder
                if self.n2 > 9:
                    if val is None: row += "__"
                    else: row += "%2i" % val
                else:
                    if val is None: row += "_"
                    else: row += str(val)
            print(row)


    ##########################################
    ####   Move Functions - YOUR IMPLEMENTATIONS GO HERE
    ##########################################

    # returns True if the space is empty and on the board,
    # and assigning val to it is not blocked by any constraints
    # space is a tuple here

    def isValidMove(self, space, val):
        row = space[0]
        col = space[-1]

        if row < 0 or row >= self.n2:
            return False
        if col < 0 or col >= self.n2:
            return False
        if val < 0 or val > self.n2:
            return False
        if val not in self.valuesInRows[row] \
                and val not in self.valuesInCols[col] \
                and val not in self.valuesInBoxes[self.spaceToBox(row, col)]\
                and space not in self.board:
            return True
        return False

    # makes a move, records it in its row, col, and box, and removes the space from unsolved
    def placeValue(self, space, val):
        row = space[0]
        col = space[-1]

        self.valuesInRows[row].add(val)
        self.valuesInCols[col].add(val)
        self.valuesInBoxes[self.spaceToBox(row, col)].add(val)
        self.unsolved.remove(space)
        self.board.update({space: val})

    # removes the move, its record in its row, col, and box, and adds the space back to unsolved
    def removeValue(self, space, val):
        row = space[0]
        col = space[-1]

        del self.board[space]
        self.valuesInRows[row].remove(val)
        self.valuesInCols[col].remove(val)
        self.valuesInBoxes[self.spaceToBox(row, col)].remove(val)
        self.unsolved.add(space)

    # optional helper function for use by getMostConstrainedUnsolvedSpace
    def evaluateSpace(self, space): #give space return number of constraints
        constrained_vals = {pos: [] for pos in self.unsolved}
        for pos, ls in constrained_vals.items():
            for i in range(1, self.n2):
                if not self.isValidMove(pos, i):
                    ls.append(i)
        return constrained_vals

    # gets the unsolved space with the most current constraints
    # returns None if unsolved is empty
    def getMostConstrainedUnsolvedSpace(self):
        constrained_vals = {pos: [] for pos in self.unsolved}
        if len(self.unsolved) == 0:
            return None

        for pos, ls in constrained_vals.items():
            for i in range(1, self.n2 + 1):
                if not self.isValidMove(pos, i):
                    ls.append(i)

        most_constrained = []
        x = 0
        for pos, ls in constrained_vals.items():
            if len(ls) > x:
                x = len(ls)

        for pos, ls in constrained_vals.items():
            if len(ls) == x:
                most_constrained.append(pos)

        return most_constrained[0]


    def unconstrainingValues(self, space):
        ls = []
        for i in range(1, self.n2 + 1):
            if self.isValidMove(space, i):
                ls.append(i)
        return ls


class Solver:
    ##########################################
    ####   Constructor
    ##########################################
    def __init__(self):
        pass

    ##########################################
    ####   Solver
    ##########################################

    # recursively selects the most constrained unsolved space and attempts
    # to assign a value to it

    # upon completion, it will leave the board in the solved state (or original
    # state if a solution does not exist)

    # returns True if a solution exists and False if one does not
    def solve(self, board):
        if board.getMostConstrainedUnsolvedSpace() is None:
            return True

        x = board.getMostConstrainedUnsolvedSpace()
        domain = board.unconstrainingValues(x)
        for v in domain:
            if board.isValidMove(x, v):
                board.placeValue(x, v)
                result = self.solve(board)
                if result:
                    return True
                board.removeValue(x, v)
        return False


if __name__ == "__main__":
    #change this to the input file that you'd like to test
    board = Board('tests/test-2-medium/01.csv')
    s = Solver()
    s.solve(board)
    board.print()




