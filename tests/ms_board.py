import unittest
from ms_board import ms_board

# TODO in wherever the gameplay section is, make sure 0 mines ends in one click
# and width * height mines ends in 0 clicks (without making the board visible?)
# TODO could have a problem with numbers of mines close to the number of the
# board, in terms of finding that random value. Could instead have a shrinking
# list of possible coordinate pairs (some indexing to linearize it), and randomly
# select from those each time. Could switch off which one is chosen on some
# saturation criteria
def count_mines(ms_board):
    return np.count_nonzeros(ms_board.board == -1)


class test_ms_board_setup(unittest.TestCase):

    def test_proper_size(self):
        board = ms_board(5, 3, 3)

    def test_mine_sanity(self):


    def test_mine_count(self):
        pass

class test_ms_neighbor_search(unittest.TestCase):

    def test_simple_case(self):
        # zero through 8
        pass

    def test_edges(self):
        pass
