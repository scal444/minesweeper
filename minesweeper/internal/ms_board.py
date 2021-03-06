import numpy as np
'''
    Contains description of a minesweeper board.
'''


class ms_board:
    '''
        Contains a minesweeper board, with state.

        Args:
            height(int): height of board
            width (int): width of board
            n_mines(int): number of mines with which to populate board
        Attributes:
            board (np.array:int) : board describing mines and number of neighboring mines
    '''

    def __init__(self, height, width, n_mines):

        if height <= 0:
            raise ValueError("Height set to {} - must be positive integer".format(height))
        if width <= 0:
            raise ValueError("Width set to {} - must be positive integer".format(width))
        if n_mines < 0:
            raise ValueError("Number of mines set to {} - must be 0 or positive integer".format(n_mines))
        if n_mines > height * width:
            raise ValueError("More mines chosen than height * width.")

        self.board = np.zeros((height, width), dtype=int)
        self._populate_board(n_mines)
        self._assign_neighbors()

    def _populate_board(self, n_mines):
        # TODO could have a problem with numbers of mines close to the number of the
        # board, in terms of finding that random value. Could instead have a shrinking
        # list of possible coordinate pairs (some indexing to linearize it), and randomly
        # select from those each time. Could switch off which one is chosen on some
        # saturation criteria
        mines_left = n_mines
        height, width = self.dimensions()
        while mines_left > 0:
            i, j = np.random.randint(0, height), np.random.randint(0, width)
            if not self.is_mine(i, j):
                self.board[i, j] = -1
                mines_left -= 1

    def dimensions(self):
        return self.board.shape

    def is_mine(self, y, x):
        return self.board[y, x] == -1

    def _assign_neighbors(self):
        '''
            Populates a board of zeros and mines with proper minesweeper counts
            of the number of neighboring mines
        '''
        for i in range(self.board.shape[0]):
            for j in range(self.board.shape[1]):
                if self.is_mine(i, j):
                    continue
                assert self.board[i, j] == 0, "overriding a nonzero neighbor count"
                neighboring_mines = 0
                for pair in self.neighbors(i, j):
                    if self.is_mine(*pair):
                        neighboring_mines += 1
                self.board[i, j] = neighboring_mines
        assert self.board.min() >= -1
        assert self.board.max() <= 8

    def neighbors(self, y_probe, x_probe):
        '''
            Calculates the neighboring grid points for a given board coordinate
            value. Handles board edges.

            Parameters:
                y - height of grid point
                x - width of grid point
            Returns:
                List of grid coordinates of neighbors, as tuples of (y, x)

            TODO does this work with size 1 boards?
        '''
        ydim, xdim = self.dimensions()

        # assertion, because we should never call neighbors with wrong parameters,
        # and the user shouldn't have access to this
        assert y_probe >= 0 and y_probe < ydim
        assert x_probe >= 0 and x_probe < xdim

        potential_y = [y for y in range(y_probe - 1, y_probe + 2) if y >= 0 and y < ydim]
        potential_x = [x for x in range(x_probe - 1, x_probe + 2) if x >= 0 and x < xdim]
        return[(y, x) for y in potential_y for x in potential_x if (y != y_probe or x != x_probe)]
