import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QWidget, QPushButton
from ms_button import ms_button
from copy import deepcopy


class ms_visual(QWidget):
    def __init__(self, runner, board, visible_mask):
        super().__init__()
        self._board = board
        self._visible_mask = visible_mask
        self._runner = runner

        self._dims = board.dimensions()
        self._create_board()

    def _create_board(self):
        self._squares = []
        for i in range(self._dims[0]):
            self.squares.append([])
            for j in range(self._dims[1]):
                self.squares[i][j] = ms_button((i,j), False, 0, self)


    def click_action(self, indices):
        print('ms board click ' + str(indices))
        self._board.process_action(indices)
