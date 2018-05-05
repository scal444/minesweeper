import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from ms_button import ms_button

class ms_board(Qwidget):
    def __init__(self, dims, n_mines):
        self.setGeometry(300, 300, dims[0] * ms_button.square_size, dims[1] * ms_button.square_size )

        self.dims = dims
        self.n_mines = n_mines
        self.is_mine = np.zeros(dims, dtype=bool)
        self.n_neighboring_mines = np.zeros(dims, dtype=int)
        self.has_been_clicked = np.zeros(dims, dtype=bool)
        self.enabled = np.ones(dims, dtype=bool)
        self.neighborlist = [[[] for i in range(dims[1])] for j in range(dims[0])]
        self.squares      = [[[] for i in range(dims[1])] for j in range(dims[0])]
        self.create_board()
        self.first_click = False
        print('initialized board')
        for i in range(dims[0]):
            for j in range(dims[1]):
                self.neighborlist[i][j] = [(a,b) for a in [i-1, i, i+1]
                                           for b in [j-1, j, j+1]
                                           if a >=0 and a < dims[0]
                                           and b >=0 and b < dims[1]
                                           and (a is not i or b is not j) ]

    def create_board(self):
        for i in range(self.dims[0]):
            for j in range(self.dims[1]):
                self.squares[i][j] = ms_button((i,j), False, 0, self)

    def run_program(self):
        print('Executing')
        self.app.exec_()

    def update_square(self, i, j):
        self.squares[i][j].is_mine = self.is_mine[i,j]
        self.squares[i][j].n_neighboring_mines = self.n_neighboring_mines[i,j]
        self.squares[i][j].has_been_clicked = self.has_been_clicked[i,j]
        self.squares[i][j].enabled = self.enabled[i,j]
        self.squares[i][j].update_visibility()

    def update_squares(self):
        for i in range(self.dims[0]):
            for j in range(self.dims[1]):
                self.update_square(i,j)

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

    def show_all_mines(self):
        for i in range(self.dims[0]):
            for j in range(self.dims[1]):
                if self.is_mine[i,j]:
                    self.squares[i][j].has_been_clicked = True
                    self.update_square(i,j)

    def freeze_board(self):
        for i in range(self.dims[0]):
            for j in range(self.dims[1]):
                self.squares[i][j].enabled = False
                self.update_square(i,j)

    def click_action(self, indices):
        print('ms board click ' + str(indices))
        y, x = indices
        self.squares[y][x].has_been_clicked = True
        self.squares[y][x].enabled = False
        if self.first_click:
            self.populate_board(indices)
            self.calc_neighboring_mines()
        if self.is_mine[y,x]:
            self.show_all_mines()
            self.freeze_board()
        elif self.n_neighboring_mines[y,x] == 0:
            for neighbor_ind in self.neighborlist[y][x]:
                 self.click_action(neighbor_ind)
        self.squares[y][x].update_visibility()
