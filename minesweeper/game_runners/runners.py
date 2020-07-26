from abc import ABC, abstractclassmethod
from internal.ms_board import ms_board
from visualization.ms_visual import ms_visual
from PyQt5.QtWidgets import QApplication


class Runner(ABC):

    @abstractclassmethod
    def run(self):
        pass


class Interactive_runner(Runner):

    def __init__(self):
        self. _app = QApplication([])
        self._board = ms_board(*board_size, n_mines)
        self._visual = ms_visual(self, self._board)

    def run(self):
        self._visual.show()
        _app.exec()
