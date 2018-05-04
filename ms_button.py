from PyQt5.QtWidgets import QPushButton


class ms_button(QPushButton):

    def __init__(self, position, is_mine, n_neighboring_mines, parent, board, is_visible=False):

        super().__init__(parent)
        self.board = board
        self.position = position
        self.is_mine = is_mine
        self.n_neighboring_mines = n_neighboring_mines


        # point to click functionality
        self.clicked.connect(self.click)
        self.update_visibility("", False)

        self.resize(square_size, square_size)
        self.move(square_size * position[0], square_size * position[1])


    def update_visibility(self, text, isvisible=False):
        self.setText(text)
        if isvisible:
            self.setStyleSheet("background-color:rgb(169,169,169)")
        else:
            self.setStyleSheet("background-color:rgb(211,211,211)")

    def click(self):
        if self.board.first_click:
            self.board.click_action(self.position)
