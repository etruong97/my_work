##################################
# State Class
##################################


class State:
    """
        This class represents the state of each board in the game

        board - the actual board that belongs to this state (See Board Class)
        parent - the State that the current State came from after applying a legal move
        depth - the depth in the move tree from the original board that this board
                can be found in (the # of moves the puzzle has undergone)
        f-value - the priority order of the state; some evaluation function of the state
    """

    # The representation of the current game state
    def __init__(self, board, parent, depth, f_value=0):
        self.board = board
        self.parent = parent
        self.depth = depth
        self.f_value = f_value

    # checks if the f-value of this board is less than the f-value of another board
    def __lt__(self, other):
        return self.f_value < other.f_value

    # converts this State into a string
    def __str__(self):
        return f"{self.board}\nf-value: {self.f_value}\nsteps: {self.depth}\n"

    # a function to explain how the state is made
    def __repr__(self):
        if self.parent is self:
            return f'State({self.board!r}, "is own parent", {self.depth!r}, {self.f_value!r})'
        try:
            return f'State({self.board!r}, {self.parent!r}, {self.depth!r}, {self.f_value!r})'
        except RecursionError:
            return 'State("could not be represented due to RecursionError")'

    # checks if two States are the same
    def __eq__(self, other):
        if type(other) is not State:
            return False
        return self.board == other.board

    # Function to print a completed path from the initial state to the solution state #
    def printPath(self):
        print(self.board)
        if self.parent is not None:
            self.parent.printPath()

    def __hash__(self):
        # this is necessary because we added an __eq__ method.
        # note that this means that you might have two State
        # instances that are "equal" but are counted as separate
        # keys in a dictionary
        return object.__hash__(self)
