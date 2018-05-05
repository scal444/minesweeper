import sys
from ms_button import ms_button
from ms_board import ms_board


beginner_n_mines = 10
beginner_dims = ( 10, 8)

dims = beginner_dims


square_size = 30
window_dims = (square_size * dims[0], square_size * dims[1])
# ------------------------------------------------------------------------



def main():
    test = ms_board((10,8), 10)
    test.create_board()
    test.show_board()
    sys.exit(test.app.exec_())

if __name__ == "__main__":
    main()
