import numpy as np
from PyQt5.QtWidgets import QWidget, QPushButton

__all__ = ["ms_visual"]


class ms_button(QPushButton):
    ''' Aesthetics and visual things are class attributes '''
    text_colors = {
        1: "(0,0,255)",
        2: "(0,255,0)",
        3: "(255,0,0)",
        4: "(75,0,130)",
        5: "(128,0,0)",
        6: "(64,224,208)",
        7: "(0,0,0)",
        8: "(0,0,255)"
    }
    background_colors = {
        'clicked': "(169,169,169)",
        'unclicked': "(211,211,211)",
        'bomb': "(255,0,0)"
    }
    square_size = 30

    def __init__(self, widget, position, text, is_visible, is_clickable=True):
        super().__init__(widget)
        self._position = position
        self._text = text
        self._is_visible = is_visible
        self._is_clickable = is_clickable
        self._widget = widget

        self.resize(self.square_size, self.square_size)
        self.move(self.square_size * self._position[1], self.square_size * self._position[0])

        self.clicked.connect(self.click_action)

    def click_action(self):
        '''
            When clicked, send signal to widget with position, only if the button
            is clickable
        '''
        if self._is_clickable:
            self._widget.click_action(self._position)

    def set_visible(self, visibility):
        assert type(visibility) == bool
        self._is_visible = visibility

    def update_visibility(self, bomb_goes_boom=False):
        if bomb_goes_boom:
            self.setStyleSheet("background-color:rgb{:s}".format(self.background_colors['bomb']))
            self.setStyleSheet("color:rgb(0,0,0)")
            self.setText('X')
            return

        if self._is_visible:
            self.setStyleSheet("background-color:rgb{:s}".format(self.background_colors['bomb']))
            self.setStyleSheet("color:rgb(0,0,0)")
            self.setText(self._text)

        else:  # unclicked
            self.setStyleSheet("background-color:rgb{:s}".format(self.background_colors['unclicked']))
            self.setText("")


class ms_visual(QWidget):
    '''
        Visualization class for a minesweeper board. Controls what the user sees
        at any time. Has access to an ms_board, which it can draw with
        specified visibilities.
    '''

    def __init__(self, runner, board, visibility=None, button_spacing=300):
        '''
            Parameters
                board(ms_board) the game board to be drawn
                visibility (np.array:bool) visibility, defaults to invisible
        '''
        super().__init__()
        self._board = board
        self._runner = runner
        dimensions = board.dimensions()
        if visibility:
            if visibility.shape != dimensions:
                raise ValueError("given visibility and board with different shapes")
            self._visibility = dimensions.astype(bool)
        else:
            self._visibility = np.zeros(board.dimensions(), dtype=bool)
        self._create_buttons()
        self.setGeometry(300, 300,
                         dimensions[1] * ms_button.square_size,
                         dimensions[0] * ms_button.square_size)

    def _create_buttons(self):
        ydim, xdim = self._dimensions()
        self._squares = [[ms_button(self, (y, x), self._board.neighbors(y, x), self._visibility[y, x])
                          for x in range(xdim)] for y in range(ydim)]

    def _dimensions(self):
        return self._board.dimensions()

    def click_action(self, indices):
        print('ms board click ' + str(indices))
        self._runner.click_action(indices)
