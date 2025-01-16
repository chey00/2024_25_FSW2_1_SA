from PyQt6.QtCore import pyqtSlot, QDateTime, pyqtSignal
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTextBrowser

from ChartView import ChartView


class CentralWidget(QWidget):

    def __init__(self, parent=None):
        super(CentralWidget, self).__init__(parent)

        chart_view = ChartView(parent)

        self.__text_browser = QTextBrowser()

        layout = QVBoxLayout()

        layout.addWidget(chart_view)
        layout.addWidget(self.__text_browser)

        self.setLayout(layout)
