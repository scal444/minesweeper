# import context
import unittest
import numpy as np
from minesweeper.ms_board import ms_board

# TODO in wherever the gameplay section is, make sure 0 mines ends in one click
# and width * height mines ends in 0 clicks (without making the board visible?)

def count_mines(ms_board):
    return np.count_nonzero(ms_board.board == -1)


class test_ms_board_setup(unittest.TestCase):

    def test_proper_size(self):
        board = ms_board(5, 3, 3)
        self.assertEqual(board.board.shape, (5, 3))

    def test_size_sanity(self):
        ms_board(5, 1, 2)
        ms_board(1, 5, 2)
        with self.assertRaises(ValueError):
            ms_board(0, 1, 1)
        with self.assertRaises(ValueError):
            ms_board(1, 0, 1)
        with self.assertRaises(ValueError):
            ms_board(-1, 5, 1)

    def test_mine_sanity(self):
        ms_board(5, 5, 0)
        ms_board(5, 5, 25)
        with self.assertRaises(ValueError):
            ms_board(5, 5, -1)
        with self.assertRaises(ValueError):
            ms_board(5, 6, 31)

    def test_mine_count(self):
        for i in range(11):
            board = ms_board(5, 2, i)
            self.assertEqual(count_mines(board), i)


class test_ms_neighbor_search(unittest.TestCase):

    def setUp(self):
        self.board = ms_board(3, 4, 0)

    @staticmethod
    def compare_neighborlists(list1, list2):
        '''
            Used for list comparison
        '''
        return sorted(list1) == sorted(list2)

    def test_simple_case(self):
        central_neighbors = self.board.neighbors(1, 2)
        self.assertEqual(len(central_neighbors), 8)
        correct_neighbors = [(1, 1),(1, 2),(1, 3),
                             (2, 1),(2, 3),
                             (3, 1),(3, 2),(3, 3 )]
        self.compare_neighborlists(central_neighbors, correct_neighbors)

    def test_edges(self):
        # bottom left
        neighbors = self.board.neighbors(0, 0)
        correct_neighbors = [(0, 1), (1, 0), (1, 1)]
        self.assertTrue(self.compare_neighborlists(neighbors, correct_neighbors))
        # left
        neighbors = self.board.neighbors(1, 0)
        correct_neighbors = [(0, 0), (0, 1), (1, 1), (2, 1), (2, 0)]
        self.assertTrue(self.compare_neighborlists(neighbors, correct_neighbors))
        # top left
        neighbors = self.board.neighbors(2, 0)
        correct_neighbors = [(1, 0), (1, 1), (2, 1)]
        self.assertTrue(self.compare_neighborlists(neighbors, correct_neighbors))
        # top
        neighbors = self.board.neighbors(2, 1)
        correct_neighbors = [(2, 0), (1, 0), (1, 1), (1, 2), (2, 2)]
        self.assertTrue(self.compare_neighborlists(neighbors, correct_neighbors))
        # top right
        neighbors = self.board.neighbors(2, 3)
        correct_neighbors = [(2, 2), (1, 2), (1, 3)]
        self.assertTrue(self.compare_neighborlists(neighbors, correct_neighbors))
        # right
        neighbors = self.board.neighbors(1, 3)
        correct_neighbors = [(2, 3), (0, 3), (0, 2), (1, 2), (2, 2)]
        self.assertTrue(self.compare_neighborlists(neighbors, correct_neighbors))
        # bottom right
        neighbors = self.board.neighbors(0, 3)
        correct_neighbors = [(1, 3), (1, 2), (0, 2)]
        self.assertTrue(self.compare_neighborlists(neighbors, correct_neighbors))
        # bottom

class test_board_neighbor_counts(unittest.TestCase):

    def setUp(self):
        self.board = ms_board(3, 3, 0)

    def test_does_not_override_mine(self):
        self.board.board[0, 0] = -1
        self.board.board[1, 1] = -1
        self.board._assign_neighbors()
        self.assertEqual(self.board.board[0, 0], -1)

    def test_zero_neighbors(self):
        self.board._assign_neighbors()
        self.assertEqual(self.board.board[1, 1], 0)

    def test_1_neighbor(self):
        self.board.board[0, 0] = -1
        self.board._assign_neighbors()
        self.assertEqual(self.board.board[1, 1], 1)

    def test_4_neighbors(self):
        self.board.board[0, 0] = -1
        self.board.board[1, 0] = -1
        self.board.board[0, 1] = -1
        self.board.board[0, 2] = -1
        self.board._assign_neighbors()
        self.assertEqual(self.board.board[1, 1], 4)

    def test_8_neighbors(self):
        self.board.board[0, 0] = -1
        self.board.board[0, 1] = -1
        self.board.board[0, 2] = -1
        self.board.board[1, 0] = -1
        self.board.board[1, 2] = -1
        self.board.board[2, 0] = -1
        self.board.board[2, 1] = -1
        self.board.board[2, 2] = -1
        self.board._assign_neighbors()
        self.assertEqual(self.board.board[1, 1], 8)

if __name__ == "__main__":
    unittest.main()
