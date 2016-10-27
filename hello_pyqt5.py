#!/usr/bin/env python3

import sys

from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Widgets
        self.button = QPushButton('Test', self)
        self.button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        # Layout
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(5, 5, 5, 5)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        # Callbacks
        self.button.clicked.connect(self.on_button)

        self.show()

    @pyqtSlot()
    def on_button(self):
        print('PyQt5 callback')


app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())
