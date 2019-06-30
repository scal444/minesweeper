import sys
from minesweeper.visualization.with_qt import ms_visual
from minesweeper import ms_board
from PyQt5.QtWidgets import QApplication


beginner_n_mines = 10
beginner_dims = ( 10, 8)

dims = beginner_dims


square_size = 30
window_dims = (square_size * dims[0], square_size * dims[1])
# ------------------------------------------------------------------------
class ms_interactive_runner:
    def __init__(self, **game_args):
        self.board = ms_board(**game_args)
        self.visual_rep = QApplication(self.board.dimensions())



    def run_app(self):
        app = Qapplication([])
        sys.exit(app.exec_())


def main():
    app = QApplication([])
    test = ms_board(10, 8, 10)
    test.show_board()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
