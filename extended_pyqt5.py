#!/usr/bin/env python3

import sys
from time import sleep

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from sip import SIP_VERSION_STR


# noinspection PyArgumentList
class Signals(QObject):
    update = pyqtSignal(int)
    worker_finished = pyqtSignal()


# noinspection PyCallByClass,PyTypeChecker,PyArgumentList
class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('PyQt5')

        self.worker_thread = QThread()
        self.worker_thread.run = self.worker
        self.worker_thread.should_close = False

        # Widgets
        self.button_start = QPushButton('Start', self)
        self.button_start.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button_stop = QPushButton('Stop', self)
        self.button_stop.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.button_stop.setDisabled(True)
        self.progress = QProgressBar(self)
        self.progress.setTextVisible(False)

        self.menu = QMenu()
        self.menu.addAction(QIcon.fromTheme('application-exit'), 'Close', QApplication.quit)

        self.status_icon = QSystemTrayIcon(QIcon('star.ico'))
        self.status_icon.setContextMenu(self.menu)
        self.status_icon.show()

        # Layout
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(5, 5, 5, 5)
        self.layout.addWidget(self.button_start)
        self.layout.addWidget(self.button_stop)
        self.layout.addWidget(self.progress)
        self.setLayout(self.layout)

        # Callbacks
        self.signals = Signals()
        self.signals.update.connect(self.on_update)
        self.signals.worker_finished.connect(self.on_worker_finished)
        self.button_start.clicked.connect(self.on_button_start)
        self.button_stop.clicked.connect(self.on_button_stop)

        self.show()

    @pyqtSlot(int)
    def on_update(self, i):
        self.progress.setValue(i)
        self.progress.update()

    @pyqtSlot()
    def on_worker_finished(self):
        self.worker_thread.should_close = False
        self.button_start.setEnabled(True)
        self.button_stop.setDisabled(True)

    # Override
    def closeEvent(self, event):
        self.worker_thread.should_close = True
        self.worker_thread.wait()
        self.status_icon.hide()

    @pyqtSlot()
    def on_button_start(self):
        self.button_start.setDisabled(True)
        self.button_stop.setEnabled(True)
        self.worker_thread.start()

    @pyqtSlot()
    def on_button_stop(self):
        self.worker_thread.should_close = True
        self.worker_thread.wait()

    def worker(self):
        for i in range(101):
            if self.worker_thread.should_close:
                break
            self.signals.update.emit(i)
            sleep(0.05)
        self.signals.worker_finished.emit()


print('PyQt', PYQT_VERSION_STR)
print('Qt', QT_VERSION_STR)
print('SIP', SIP_VERSION_STR)
app = QApplication(sys.argv)
win = Window()
sys.exit(app.exec_())
