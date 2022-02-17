# importing required libraries
from PySide2.QtCore import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtWebEngineWidgets import *
import os
import sys


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://localhost:19006/'))

        self.border = QLabel(self.browser)
        self.border.setHidden(True)
        self.fringe = QLabel(self.browser)
        self.fringe.setHidden(True)

        self.setWindowIcon(QIcon(QPixmap(self.get_path('icon.ico'))))
        self.setCentralWidget(self.browser)
        self.ratio = (16 / 9)

        self.toolbar = QToolBar(self)
        print(self.toolbar.height(), self.toolbar.orientation())

        set_ratio_16_9 = QAction('16:9', self.toolbar)
        set_ratio_16_9.triggered.connect(lambda: self.set_ratio(16 / 9))

        set_ratio_20_9 = QAction('20:9', self.toolbar)
        set_ratio_20_9.triggered.connect(lambda: self.set_ratio(20 / 9))

        set_ratio_21_9 = QAction('21:9', self.toolbar)
        set_ratio_21_9.triggered.connect(lambda: self.set_ratio(21 / 9))

        refresh = QAction('↺', self.toolbar)
        refresh.triggered.connect(self.browser.reload)

        border_cb = QCheckBox('Border', self.toolbar)
        border_cb .stateChanged.connect(self.refresh_border)

        fringe_cb = QCheckBox('Fringe', self.toolbar)
        fringe_cb .stateChanged.connect(self.refresh_fringe)

        self.url_edit = QLineEdit(self.toolbar)
        self.url_edit.returnPressed.connect(
            lambda: self.browser.setUrl(QUrl(self.url_edit.text()))
        )

        self.toolbar.addAction(refresh)
        self.toolbar.addWidget(self.url_edit)
        self.toolbar.addSeparator()
        self.toolbar.addWidget(border_cb)
        self.toolbar.addWidget(fringe_cb)
        self.toolbar.addSeparator()
        self.toolbar.addAction(set_ratio_16_9)
        self.toolbar.addAction(set_ratio_20_9)
        self.toolbar.addAction(set_ratio_21_9)

        self.addToolBar(self.toolbar)

        self.show()

    def get_path(self, file):
        if hasattr(sys, '_MEIPASS'):
            return os.path.join(sys._MEIPASS, file)
        else:
            return os.path.join(os.path.abspath("."), file)

    def set_ratio(self, ratio):
        self.ratio = ratio

        if self.toolbar.orientation() == Qt.Orientation.Horizontal:
            height = self.width() * self.ratio + self.toolbar.height()
        else:
            height = (self.width() - self.toolbar.width()) * self.ratio

        self.setGeometry(
            self.x(),
            self.y(),
            self.width(),
            height
        )

        self.resize_pixmaps()

        self.browser.reload()

    def refresh_border(self, state):
        self.border.setHidden(state == 0)
        self.resize_pixmaps()

    def refresh_fringe(self, state):
        self.fringe.setHidden(state == 0)
        self.resize_pixmaps()

    def resize_pixmaps(self):
        pixmap = QPixmap(self.get_path('border.png')).scaled(
            self.browser.width(), self.browser.height()
        )
        self.border.setPixmap(pixmap)
        self.border.resize(pixmap.width(), pixmap.height())

        pixmap = QPixmap(self.get_path('fringe.png')).scaled(
            self.browser.width(), self.browser.height()
        )
        self.fringe.setPixmap(pixmap)
        self.fringe.resize(pixmap.width(), pixmap.height())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName('React Previewer')
    window = MainWindow()
    window.resize(360, 640)
    app.exec_()
