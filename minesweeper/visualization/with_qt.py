import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from ms_button import ms_button
from copy import deepcopy


class ms_visual(QWidget):
    def __init__(self, board, visible_mask):
        super().__init__()
        self.board = board
        self.visible_mask = visible_mask
