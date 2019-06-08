import sys
from ms_button import ms_button
from ms_board import ms_board
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


beginner_n_mines = 10
beginner_dims = ( 10, 8)

dims = beginner_dims


square_size = 30
window_dims = (square_size * dims[0], square_size * dims[1])
# ------------------------------------------------------------------------



def main():
    app = QApplication([])
    test = ms_board((10,8), 10)
    test.show_board()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
