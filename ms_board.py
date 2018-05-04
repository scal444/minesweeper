import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class ms_board:
    def __init__(self, dims, n_mines):
        self.app = QApplication(sys.argv)
        self.widg = QWidget()
        self.widg.setGeometry(300, 300, *window_dims)

        self.dims = dims
        self.n_mines = n_mines
        self.is_mine = np.zeros(dims, dtype=bool)
        self.is_visible = np.zeros(dims, dtype=bool)
        self.n_neighboring_mines = np.zeros(dims, dtype=int)
        self.neighborlist = [[[] for i in range(dims[1])] for j in range(dims[0])]
        self.squares      = [[[] for i in range(dims[1])] for j in range(dims[0])]

        self.first_click = False

        for i in range(dims[0]):
            for j in range(dims[1]):
                self.neighborlist[i][j] = [(a,b) for a in [i-1, i, i+1]
                                           for b in [j-1, j, j+1]
                                           if a >=0 and a < dims[0]
                                           and b >=0 and b < dims[1]
                                           and (a is not i or b is not j) ]

    def create_board(self):
        for i in range(dims[0]):
            for j in range(dims[1]):
                self.squares[i][j] = ms_button((i,j), False, 0, self.widg, self)

    def update_squares(self):
        for i in range(self.dims[0]):
            for j in range(self.dims[1]):
                if self.is_visible[i, j]:
                    if self.ismine[i,j]:
                        self.squares[i][j].update_visibility('X', True)
                    elif self.n_neighboring_mines[i,j] > 0:
                        self.squares[i][j].update_visibility(self.n_neighboring_mines[i,j], True)
                    else:
                        self.squares[i][j].update_visibility("", True)
                else:
                    self.squares[i][j].update_visibility("", False)

    def populate_board(self, first_indices):
        '''
            The board is only populated after the first click, as the first
            square clicked cannot be a mine, nor can any surrounding it

            First indices is a tuple of down, across indices

        '''
        mines_left = self.n_mines
        while mines_left > 0:
            i, j = np.random.randint(0, self.dims[0]), np.random.randint(0, self.dims[1])
            if np.abs(first_indices[0] - i) > 1 and np.abs(first_indices[1] - j) > 1 and not self.is_mine[i,j]:
                self.is_mine[i,j] = True
                self.squares[i][j].is_mine = True
                mines_left -= 1


    def calc_neighboring_mines(self):
        for i in range(self.dims[0]):
            for j in range(self.dims[1]):
                mines = 0
                for down,across in self.neighborlist[i][j]:
                    if self.is_mine[down, across]:
                        mines += 1
                self.n_neighboring_mines[i,j] = mines
                self.squares[i][j].n_neighboring_mines = mines

    def show_board(self):
        self.update_squares()
        self.widg.update()
        self.widg.show()


    def plot_underlying_board(self):
        for i in range(self.dims[0]):
            for j in range(self.dims[1]):


                if self.is_mine[i,j]:
                    plt.text(j + .5, i + .5, 'X', color='r')
                elif self.n_neighboring_mines[i,j] > 0:
                    plt.text(j + .5 , i + .5, str(self.n_neighboring_mines[i,j]))
        plt.axis('off')


        for i in range(self.dims[0] + 1):
            plt.hlines(i, 0, dims[1])
        for i in range(self.dims[1] + 1):
            plt.vlines(i, 0, dims[0])
        plt.show()

    def click_action(self, indices):
        if self.first_click:
            self.populate_board(indices)
            self.calc_neighboring_mines()
        if self.is_mine[i,j]:
            self.squares[indices[0]][indices[1]].update_visibility('X', True)
        elif self.n_neighboring_mines[i,j] > 0:
            self.squares[indices[0]][indices[1]].update_visibility(str(self.n_neighboring_mines[i,j]), True)
        else:
            for i,j in
