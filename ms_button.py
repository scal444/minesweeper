from PyQt5.QtWidgets import QPushButton


class ms_button(QPushButton):

    text_colors = {
        1 : "(0,0,255)",
        2 : "(0,255,0)",
        3 : "(255,0,0)",
        4 : "(75,0,130)",
        5 : "(128,0,0)",
        6 : "(64,224,208)",
        7 : "(0,0,0)",
        8 : "(0,0,255)"
    }
    background_colors = {
        'clicked'   : "(169,169,169)",
        'unclicked' : "(211,211,211)",
        'bomb'      : "(255,0,0)"
    }

    def __init__(self, position, is_mine, n_neighboring_mines, widget, board,
                 has_been_clicked=False, enabled=True):



        super().__init__(widget)
        self.board = board
        self.position = position
        self.is_mine = is_mine
        self.n_neighboring_mines = n_neighboring_mines
        self.has_been_clicked = has_been_clicked
        self.setEnabled(enabled)  # should be enabled at start for typical game

        # point to click functionality
        self.clicked.connect(self.click_action)
        self.update_visibility()

        self.resize(square_size, square_size)
        self.move(square_size * position[0], square_size * position[1])

    def set_underlying_text(self):
        if self.is_mine:
            self.text = 'X'
        elif self.n_neighboring_mines == 0:
            self.text = ''
        else:
            self.text = str(self.n_neighboring_mines)

    def update_visibility(self):
        if isvisible:
            if self.is_mine:
                self.setStyleSheet("background-color:rgb{:s}".format(self.background_colors['bomb']))
                self.setStyleSheet("color:rgb(0,0,0)")
                self.setText('X')
            else:
                self.setStyleSheet("background-color:rgb{:s}".format(self.background_colors['clicked']))
                self.setStyleSheet("color:rgb{:s}".format(self.text_colors[self.n_neighboring_mines]))
                self.setText(str(self.n_neighboring_mines))
        else: # unclicked
            self.setStyleSheet("background-color:rgb{:s}".format(self.background_colors['unclicked']))
            self.setText("")

    def click_action(self):
        if self.board.first_click:
            self.board.click_action(self.position)
