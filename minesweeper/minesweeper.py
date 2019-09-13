import sys
from internal.ms_board import ms_board
from visualization.ms_visual import ms_visual
from PyQt5.QtWidgets import QApplication


class default_runner(object):
    ''' Runner for a minesweeper game '''

    def __init__(self, board_size, n_mines):
        self._board = ms_board(*board_size, n_mines)
        self._visual = ms_visual(self, self._board)
        self._visual.show()

    def click_action(self, position):
        print("click at position y = {}, x = {}".format(*position))


def minesweeper():
    app = QApplication([])
    default_runner((10, 8), 8)
    sys.exit(app.exec_())


def main():
    minesweeper(sys.argv[1])


if __name__ == "__main__":
    main()
