import numpy as np
from copy import deepcopy
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
            board (np.array:int) :
            visibility (np.array:int) :
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

        self.board      = np.zeros((height, width))
        self.visibility = np.zeros((width, height))
        self._populate_board(n_mines)
        self._assign_neighbors()

    def _populate_board(self, n_mines):
        mines_left = n_mines
        height, width = self.dimensions()
        while mines_left > 0:
            i, j = np.random.randint(0, height), np.random.randint(0, width)
            if not self._is_mine(i, j):
                self.board[i, j] = -1
                mines_left -= 1

    def dimensions(self):
        return self.board.shape

    def _is_mine(self, y, x):
        return self.board[y, x] == -1

    def _assign_neighbors(self):
        '''
            Populates a board of zeros and mines with proper minesweeper counts
            of the number of neighboring mines
        '''

    def neighbors(self, y_probe, x_probe):
        '''
            Calculates the neighboring grid points for a given board coordinate
            value. Handles board edges.

            Parameters:
                y - height of grid point
                x - width of grid point
            Returns:
                List of grid coordinates of neighbors, as tuples of (y, x)
        '''
        ydim, xdim = self.dimensions()

        # assertion, because we should never call neighbors with wrong parameters,
        # and the user shouldn't have access to this
        assert y_probe >= 0 and y_probe < ydim
        assert x_probe >= 0 and x_probe < xdim

        potential_y = [y for y in range(y_probe -1, y_probe + 2) if y >= 0 and y < ydim]
        potential_x = [x for x in range(x_probe -1, x_probe + 2) if x >= 0 and x < xdim]
        return[(y, x) for y in potential_y for x in potential_x if (y != y_probe or x != x_probe)]
