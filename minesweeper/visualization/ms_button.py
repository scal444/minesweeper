from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


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

    def __init__(self, widget, position, text_representation,
                 is_visible=False, is_clickable=True):

        super().__init__(board)
        self._position = position
        self._text_representation = test_representation
        self._is_visible = has_been_clicked
        self._is_clickable = enabled
        self._text = text

        # point to click functionality
        self.clicked.connect(self.click_action)

        # visual stuff
        self.resize(self.square_size, self.square_size)
        self.move(self.square_size * self._position[0], self.square_size * self._position[1])

    def click_action(self):
        '''
            When clicked, sends signal to widget, only if this button is clickable
        '''
        if self._is_clickable():
            self._widget.click_action(self._position)

    def update_visibility(self, override_with_bomb=False):
        if override_with_bomb:
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
