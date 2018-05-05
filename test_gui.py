import ms_runner
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from ms_board import ms_board
from ms_button import ms_button
'''
    Creates minesweeper boards with various options, to check how the gui is
    working. Math and underlying code tests are in "test_modules.py"
'''

def test_uninitialized_board():
    test_board = ms_board( (10,8), 10)
    test_board.create_board()
    test_board.show_board()
